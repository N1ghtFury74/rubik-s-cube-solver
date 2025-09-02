"""
Professional GUI for Rubik's Cube Color Input
Provides an intuitive interface for inputting cube colors
"""

import tkinter as tk
from tkinter import colorchooser, messagebox
import logging
from typing import Callable, Optional
from ..config.settings import WINDOW_TITLE, CANVAS_SIZE, GRID_SPACING
from ..core.cube_solver import CubeSolver
from ..communication.arduino_interface import ArduinoInterface

logger = logging.getLogger(__name__)


class CubeInputGUI:
    """
    Professional GUI for Rubik's cube color input and robot control
    """
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(WINDOW_TITLE)
        
        # Core components
        self.solver = CubeSolver()
        self.arduino = ArduinoInterface()
        
        # GUI state
        self.current_face = 0
        self.face_names = ['Yellow', 'Blue', 'Red', 'Green', 'Orange', 'White']
        self.face_colors = ['#FFFF00', '#0000FF', '#FF0000', '#00FF00', '#FFA500', '#FFFFFF']
        
        self._setup_gui()
        
    def _setup_gui(self) -> None:
        """Initialize the GUI components"""
        self._create_face_buttons()
        self._create_control_buttons()
        self._create_status_display()
        
    def _create_face_buttons(self) -> None:
        """Create buttons for each cube face"""
        face_configs = [
            ('Yellow', 0, 1, '#FFFF00', self._input_yellow_face),
            ('Blue', 0, 2, '#0000FF', self._input_blue_face),
            ('Red', 0, 3, '#FF0000', self._input_red_face),
            ('Green', 0, 4, '#00FF00', self._input_green_face),
            ('Orange', 0, 5, '#FFA500', self._input_orange_face),
            ('White', 0, 6, '#FFFFFF', self._input_white_face)
        ]
        
        for name, row, col, color, command in face_configs:
            btn = tk.Button(
                self.root,
                text=f"Input {name} Face",
                command=command,
                bg=color,
                fg='black' if color == '#FFFFFF' else 'white',
                font=('Arial', 10, 'bold'),
                padx=10,
                pady=5
            )
            btn.grid(row=row, column=col, padx=2, pady=2)
    
    def _create_control_buttons(self) -> None:
        """Create control buttons for solving and communication"""
        control_configs = [
            ('Convert Colors', 0, 65, '#006069', self._convert_colors),
            ('Generate Solution', 0, 67, '#00a0b0', self._solve_cube),
            ('Send to Robot', 0, 68, '#006069', self._send_to_arduino),
            ('Send Reversed', 0, 69, '#0060DD', self._send_reversed),
            ('Test Connection', 0, 66, '#26c2e3', self._test_connection)
        ]
        
        for text, row, col, color, command in control_configs:
            btn = tk.Button(
                self.root,
                text=text,
                command=command,
                bg=color,
                fg='white',
                font=('Arial', 10, 'bold'),
                padx=10,
                pady=5
            )
            btn.grid(row=row, column=col, padx=2, pady=2)
    
    def _create_status_display(self) -> None:
        """Create status display area"""
        self.status_text = tk.Text(
            self.root,
            height=10,
            width=80,
            font=('Courier', 9)
        )
        self.status_text.grid(row=15, column=0, columnspan=70, padx=10, pady=10)
        
        # Add scrollbar
        scrollbar = tk.Scrollbar(self.root, command=self.status_text.yview)
        scrollbar.grid(row=15, column=70, sticky='nsew')
        self.status_text.config(yscrollcommand=scrollbar.set)
    
    def _input_face_colors(self, face_index: int, face_name: str) -> None:
        """
        Generic method to input colors for a cube face
        
        Args:
            face_index: Index of the face (0-5)
            face_name: Name of the face for display
        """
        colors = []
        grid_config = GRID_SPACING.get(face_name.lower(), {})
        
        self._log_status(f"Inputting colors for {face_name} face...")
        
        for i in range(9):
            color = colorchooser.askcolor(title=f"{face_name} Face - Square {i+1}/9")[1]
            if color:
                colors.append(color)
                # Create visual feedback
                row = grid_config.get('row_range', (2, 5))[0] + (i // 3)
                col = grid_config.get('col_range', (50, 53))[0] + (i % 3)
                
                canvas = tk.Canvas(
                    self.root,
                    width=CANVAS_SIZE,
                    height=CANVAS_SIZE,
                    bg=color
                )
                canvas.grid(row=row, column=col, padx=1, pady=1)
            else:
                self._log_status(f"Color input cancelled for {face_name} face")
                return
        
        self.solver.set_face_colors(face_index, colors)
        self._log_status(f"✓ {face_name} face colors saved successfully")
    
    # Face input methods
    def _input_yellow_face(self): self._input_face_colors(0, 'Yellow')
    def _input_blue_face(self): self._input_face_colors(1, 'Blue')
    def _input_red_face(self): self._input_face_colors(2, 'Red')
    def _input_green_face(self): self._input_face_colors(3, 'Green')
    def _input_orange_face(self): self._input_face_colors(4, 'Orange')
    def _input_white_face(self): self._input_face_colors(5, 'White')
    
    def _convert_colors(self) -> None:
        """Convert input colors to cube state"""
        try:
            cube_state = self.solver.convert_colors_to_state()
            if self.solver.validate_cube_state():
                self._log_status(f"✓ Cube state generated: {cube_state}")
            else:
                self._log_status("⚠ Warning: Invalid cube state detected")
        except Exception as e:
            self._log_status(f"✗ Error converting colors: {e}")
    
    def _solve_cube(self) -> None:
        """Generate solution for the cube"""
        try:
            solution = self.solver.solve_cube()
            self._log_status(f"✓ Solution generated: {solution}")
        except Exception as e:
            self._log_status(f"✗ Error solving cube: {e}")
    
    def _send_to_arduino(self) -> None:
        """Send solution moves to Arduino"""
        if not self.solver.solution_moves:
            self._log_status("✗ No solution available. Generate solution first.")
            return
            
        try:
            with self.arduino as arduino:
                if arduino.send_moves(self.solver.solution_moves):
                    self._log_status("✓ Moves sent to robot successfully")
                else:
                    self._log_status("✗ Failed to send moves to robot")
        except Exception as e:
            self._log_status(f"✗ Arduino communication error: {e}")
    
    def _send_reversed(self) -> None:
        """Send reversed moves to Arduino"""
        try:
            reversed_moves = self.solver.get_reversed_moves()
            with self.arduino as arduino:
                if arduino.send_moves(reversed_moves):
                    self._log_status("✓ Reversed moves sent to robot successfully")
                else:
                    self._log_status("✗ Failed to send reversed moves to robot")
        except Exception as e:
            self._log_status(f"✗ Error sending reversed moves: {e}")
    
    def _test_connection(self) -> None:
        """Test Arduino connection"""
        try:
            with self.arduino as arduino:
                if arduino.send_test_command():
                    self._log_status("✓ Arduino connection test successful")
                else:
                    self._log_status("✗ Arduino connection test failed")
        except Exception as e:
            self._log_status(f"✗ Connection test error: {e}")
    
    def _log_status(self, message: str) -> None:
        """
        Log status message to GUI and logger
        
        Args:
            message: Status message to display
        """
        timestamp = time.strftime("%H:%M:%S")
        formatted_message = f"[{timestamp}] {message}\n"
        
        self.status_text.insert(tk.END, formatted_message)
        self.status_text.see(tk.END)
        logger.info(message)
    
    def run(self) -> None:
        """Start the GUI application"""
        self._log_status("🤖 Rubik's Cube Solver Robot - Ready!")
        self._log_status("💡 Built by Momentum Team - 900 EGP Budget - 10-12s Solve Time")
        self._log_status("📋 Instructions: 1) Input all 6 faces 2) Convert colors 3) Generate solution 4) Send to robot")
        self.root.mainloop()
    
    def __del__(self):
        """Cleanup on destruction"""
        self.disconnect()
