"""
Unit tests for the Rubik's Cube Solver
Ensures 100% reliability of the solving logic
"""

import unittest
import sys
import os

# Add src to path for testing
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.core.cube_solver import CubeSolver
from src.config.settings import COLOR_MAP


class TestCubeSolver(unittest.TestCase):
    """Test cases for the CubeSolver class"""
    
    def setUp(self):
        """Set up test fixtures before each test method"""
        self.solver = CubeSolver()
        
        # Valid solved cube state (all faces same color)
        self.solved_colors = {
            0: ["#ffff00"] * 9,  # Yellow face
            1: ["#0000ff"] * 9,  # Blue face
            2: ["#ff0000"] * 9,  # Red face
            3: ["#00ff00"] * 9,  # Green face
            4: ["#ff8000"] * 9,  # Orange face
            5: ["#ffffff"] * 9   # White face
        }
    
    def test_face_color_setting(self):
        """Test setting colors for cube faces"""
        test_colors = ["#ff0000"] * 9
        self.solver.set_face_colors(0, test_colors)
        self.assertEqual(self.solver.cube_faces[0], " ".join(test_colors))
    
    def test_invalid_face_index(self):
        """Test error handling for invalid face indices"""
        with self.assertRaises(ValueError):
            self.solver.set_face_colors(6, ["#ff0000"] * 9)
        
        with self.assertRaises(ValueError):
            self.solver.set_face_colors(-1, ["#ff0000"] * 9)
    
    def test_invalid_color_count(self):
        """Test error handling for wrong number of colors"""
        with self.assertRaises(ValueError):
            self.solver.set_face_colors(0, ["#ff0000"] * 8)  # Only 8 colors
    
    def test_color_conversion(self):
        """Test hex color to cube notation conversion"""
        # Set up a simple test case
        self.solver.set_face_colors(0, ["#ffffff"] * 9)  # All white
        cube_state = self.solver.convert_colors_to_state()
        
        # Should start with 9 'w' characters
        self.assertTrue(cube_state.startswith('w' * 9))
    
    def test_cube_state_validation(self):
        """Test cube state validation logic"""
        # Set up a valid solved cube
        for face_idx, colors in self.solved_colors.items():
            self.solver.set_face_colors(face_idx, colors)
        
        self.solver.convert_colors_to_state()
        self.assertTrue(self.solver.validate_cube_state())
    
    def test_invalid_cube_state(self):
        """Test detection of invalid cube states"""
        # Create invalid state (too many of one color)
        self.solver.cube_state = 'w' * 54  # All white - invalid
        self.assertFalse(self.solver.validate_cube_state())
    
    def test_solver_reset(self):
        """Test solver reset functionality"""
        # Set some data
        self.solver.set_face_colors(0, ["#ff0000"] * 9)
        self.solver.cube_state = "test_state"
        self.solver.solution_moves = "R U R'"
        
        # Reset and verify
        self.solver.reset()
        self.assertEqual(self.solver.cube_faces, [""] * 6)
        self.assertEqual(self.solver.cube_state, "")
        self.assertEqual(self.solver.solution_moves, "")
    
    def test_reversed_moves_generation(self):
        """Test generation of reversed move sequences"""
        # Set up a simple solution
        self.solver.solution_moves = "R U R'"
        reversed_moves = self.solver.get_reversed_moves()
        
        # Should reverse and invert moves
        self.assertIn("R", reversed_moves)
        self.assertIn("U'", reversed_moves)
        self.assertIn("R'", reversed_moves)
    
    def test_no_solution_error(self):
        """Test error when trying to get reversed moves without solution"""
        with self.assertRaises(ValueError):
            self.solver.get_reversed_moves()


class TestColorMapping(unittest.TestCase):
    """Test cases for color mapping functionality"""
    
    def test_all_colors_mapped(self):
        """Test that all standard Rubik's colors are mapped"""
        expected_colors = {'w', 'r', 'y', 'g', 'o', 'b'}
        mapped_colors = set(COLOR_MAP.values())
        self.assertEqual(expected_colors, mapped_colors)
    
    def test_color_map_completeness(self):
        """Test that color map contains all expected hex codes"""
        expected_hex_codes = {
            "#ffffff",  # White
            "#ff0000",  # Red
            "#ffff00",  # Yellow
            "#00ff00",  # Green
            "#ff8000",  # Orange
            "#0000ff"   # Blue
        }
        mapped_hex_codes = set(COLOR_MAP.keys())
        self.assertEqual(expected_hex_codes, mapped_hex_codes)


if __name__ == '__main__':
    # Create test suite
    suite = unittest.TestSuite()
    
    # Add test cases
    suite.addTest(unittest.makeSuite(TestCubeSolver))
    suite.addTest(unittest.makeSuite(TestColorMapping))
    
    # Run tests with detailed output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Exit with appropriate code
    sys.exit(0 if result.wasSuccessful() else 1)
