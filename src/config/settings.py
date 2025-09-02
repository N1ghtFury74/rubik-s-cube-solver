"""
Configuration settings for the Rubik's Cube Solver Robot
"""

# Hardware Configuration
ARDUINO_PORT = 'COM6'
ARDUINO_BAUDRATE = 9600
ARDUINO_TIMEOUT = 3

# Stepper Motor Configuration
STEPS_PER_90_DEGREE = 50  # 50 steps for 90° rotation
STEPS_PER_180_DEGREE = 100  # 100 steps for 180° rotation
STEP_DELAY_MICROSECONDS = 1000
MOVE_DELAY_MILLISECONDS = 200

# Color Mapping (Hex to Rubik's notation)
COLOR_MAP = {
    "#ffffff": 'w',  # White
    "#ff0000": 'r',  # Red  
    "#ffff00": 'y',  # Yellow
    "#00ff00": 'g',  # Green
    "#ff8000": 'o',  # Orange
    "#0000ff": 'b'   # Blue
}

# GUI Configuration
WINDOW_TITLE = "Rubik's Cube Solver - Momentum Team"
CANVAS_SIZE = 50
GRID_SPACING = {
    'yellow': {'row_range': (2, 5), 'col_range': (50, 53)},
    'blue': {'row_range': (6, 9), 'col_range': (40, 43)},
    'red': {'row_range': (6, 9), 'col_range': (50, 53)},
    'white': {'row_range': (9, 12), 'col_range': (50, 53)},
    'green': {'row_range': (6, 9), 'col_range': (54, 57)},
    'orange': {'row_range': (6, 9), 'col_range': (58, 61)}
}

# Solver Configuration
DEFAULT_ALGORITHM = 'Kociemba'  # Options: 'Beginner', 'CFOP', 'Kociemba'
SOLVED_STATE = "L2B2R2B2F2R2D'U2B2R2BU'L'RD'B2UBRU'R"

# Performance Metrics
TARGET_SOLVE_TIME_SECONDS = 12
ROBOT_COST_EGP = 900
YEAR_BUILT = 2022
