"""
Core Rubik's Cube Solver Logic
Handles cube state management and solution generation
"""

from rubik_solver import utils
from typing import List, Optional
import logging
from ..config.settings import COLOR_MAP, DEFAULT_ALGORITHM

logger = logging.getLogger(__name__)


class CubeSolver:
    """
    Professional Rubik's Cube Solver class that manages cube state and generates solutions
    """
    
    def __init__(self):
        self.cube_faces = ["" for _ in range(6)]  # 6 faces of the cube
        self.cube_state = ""
        self.solution_moves = ""
        
    def set_face_colors(self, face_index: int, colors: List[str]) -> None:
        """
        Set colors for a specific face of the cube
        
        Args:
            face_index: Index of the face (0-5)
            colors: List of 9 hex color codes for the face
        """
        if not (0 <= face_index <= 5):
            raise ValueError(f"Face index must be between 0 and 5, got {face_index}")
        
        if len(colors) != 9:
            raise ValueError(f"Each face must have exactly 9 colors, got {len(colors)}")
            
        self.cube_faces[face_index] = " ".join(colors)
        logger.info(f"Set colors for face {face_index}")
    
    def convert_colors_to_state(self) -> str:
        """
        Convert hex color codes to Rubik's cube notation string
        
        Returns:
            54-character string representing the cube state
        """
        self.cube_state = ""
        
        for face_index in range(6):
            face_colors = self.cube_faces[face_index].split()
            
            if len(face_colors) != 9:
                logger.warning(f"Face {face_index} has {len(face_colors)} colors, expected 9")
                continue
                
            for color_hex in face_colors:
                if color_hex in COLOR_MAP:
                    self.cube_state += COLOR_MAP[color_hex]
                else:
                    logger.warning(f"Unknown color: {color_hex}")
                    self.cube_state += 'w'  # Default to white for unknown colors
        
        logger.info(f"Generated cube state: {self.cube_state}")
        return self.cube_state
    
    def solve_cube(self, algorithm: str = DEFAULT_ALGORITHM) -> str:
        """
        Generate solution moves for the current cube state
        
        Args:
            algorithm: Solving algorithm to use ('Beginner', 'CFOP', 'Kociemba')
            
        Returns:
            String of moves to solve the cube
        """
        if not self.cube_state:
            self.convert_colors_to_state()
            
        if len(self.cube_state) != 54:
            raise ValueError(f"Invalid cube state length: {len(self.cube_state)}, expected 54")
        
        try:
            self.solution_moves = utils.solve(self.cube_state, algorithm)
            logger.info(f"Generated solution with {algorithm}: {self.solution_moves}")
            return self.solution_moves
        except Exception as e:
            logger.error(f"Failed to solve cube: {e}")
            raise
    
    def get_reversed_moves(self) -> str:
        """
        Generate reversed moves to undo the solution
        
        Returns:
            String of reversed moves
        """
        if not self.solution_moves:
            raise ValueError("No solution moves available. Solve the cube first.")
        
        moves_str = "".join(map(str, self.solution_moves))
        reversed_moves = list(reversed(moves_str))
        reversed_str = ""
        
        i = 0
        while i < len(reversed_moves):
            if reversed_moves[i] == '2':
                # Handle double moves (e.g., R2 becomes R2)
                if i + 1 < len(reversed_moves):
                    reversed_str += reversed_moves[i + 1] + reversed_moves[i]
                    i += 2
                else:
                    i += 1
            elif reversed_moves[i] == '\'':
                # Handle prime moves (e.g., R' becomes R)
                if i + 1 < len(reversed_moves):
                    reversed_str += reversed_moves[i + 1]
                    i += 2
                else:
                    i += 1
            else:
                # Handle normal moves (e.g., R becomes R')
                reversed_str += reversed_moves[i] + '\''
                i += 1
        
        logger.info(f"Generated reversed moves: {reversed_str}")
        return reversed_str
    
    def validate_cube_state(self) -> bool:
        """
        Validate that the cube state is solvable
        
        Returns:
            True if the cube state is valid and solvable
        """
        if len(self.cube_state) != 54:
            return False
            
        # Count each color - should have exactly 9 of each
        color_counts = {}
        for color in self.cube_state:
            color_counts[color] = color_counts.get(color, 0) + 1
        
        expected_colors = {'w', 'r', 'y', 'g', 'o', 'b'}
        
        # Check if we have all 6 colors with 9 occurrences each
        if set(color_counts.keys()) != expected_colors:
            logger.error(f"Invalid colors in cube state: {set(color_counts.keys())}")
            return False
            
        for color, count in color_counts.items():
            if count != 9:
                logger.error(f"Color {color} appears {count} times, expected 9")
                return False
        
        return True
    
    def reset(self) -> None:
        """Reset the solver to initial state"""
        self.cube_faces = ["" for _ in range(6)]
        self.cube_state = ""
        self.solution_moves = ""
        logger.info("Solver reset to initial state")
