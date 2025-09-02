# 📚 API Reference

## Core Classes

### CubeSolver
Main solver class that handles cube state and solution generation.

#### Methods

##### `set_face_colors(face_index: int, colors: List[str]) -> None`
Set colors for a specific cube face.
- **face_index**: 0-5 (Yellow, Blue, Red, Green, Orange, White)
- **colors**: List of 9 hex color codes

##### `convert_colors_to_state() -> str`
Convert hex colors to 54-character cube state string.
- **Returns**: Cube state in standard notation (w,r,y,g,o,b)

##### `solve_cube(algorithm: str = 'Kociemba') -> str`
Generate optimal solution moves.
- **algorithm**: 'Beginner', 'CFOP', or 'Kociemba'
- **Returns**: Move sequence string

##### `get_reversed_moves() -> str`
Generate reversed moves to undo solution.
- **Returns**: Reversed move sequence

##### `validate_cube_state() -> bool`
Validate that cube state is solvable.
- **Returns**: True if valid, False otherwise

### ArduinoInterface
Handles serial communication with Arduino controller.

#### Methods

##### `connect() -> bool`
Establish Arduino connection.
- **Returns**: True if successful

##### `send_moves(moves: str) -> bool`
Send move sequence to Arduino.
- **moves**: String of cube moves
- **Returns**: True if sent successfully

##### `disconnect() -> None`
Close Arduino connection.

## Move Notation

### Standard Moves
- **R**: Right face clockwise 90°
- **R'**: Right face counter-clockwise 90°
- **R2**: Right face 180°
- **U, D, L, F, B**: Other faces follow same pattern

### Face Mapping
- **U**: Up (Top)
- **D**: Down (Bottom)  
- **L**: Left
- **R**: Right
- **F**: Front
- **B**: Back

## Configuration

### Hardware Settings
Edit `src/config/settings.py`:

```python
ARDUINO_PORT = 'COM6'           # Arduino serial port
ARDUINO_BAUDRATE = 9600         # Communication speed
STEPS_PER_90_DEGREE = 50        # Motor calibration
MOVE_DELAY_MILLISECONDS = 200   # Timing between moves
```

### Color Mapping
```python
COLOR_MAP = {
    "#ffffff": 'w',  # White
    "#ff0000": 'r',  # Red
    "#ffff00": 'y',  # Yellow
    "#00ff00": 'g',  # Green
    "#ff8000": 'o',  # Orange
    "#0000ff": 'b'   # Blue
}
```

## Error Handling

### Common Exceptions
- **ValueError**: Invalid cube state or parameters
- **SerialException**: Arduino communication failure
- **SolverError**: Algorithm cannot find solution

### Logging
All operations are logged to `logs/cube_solver.log` with timestamps and severity levels.
