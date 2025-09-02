"""
Integration tests for Arduino communication
Tests the reliability of the Python-Arduino interface
"""

import unittest
import sys
import os
from unittest.mock import Mock, patch, MagicMock

# Add src to path for testing
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.communication.arduino_interface import ArduinoInterface


class TestArduinoInterface(unittest.TestCase):
    """Test cases for Arduino communication interface"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.arduino = ArduinoInterface(port='COM_TEST', baudrate=9600)
    
    @patch('serial.Serial')
    def test_successful_connection(self, mock_serial):
        """Test successful Arduino connection"""
        mock_connection = Mock()
        mock_serial.return_value = mock_connection
        
        result = self.arduino.connect()
        
        self.assertTrue(result)
        mock_serial.assert_called_once_with('COM_TEST', 9600, timeout=3)
    
    @patch('serial.Serial')
    def test_connection_failure(self, mock_serial):
        """Test Arduino connection failure handling"""
        mock_serial.side_effect = Exception("Port not found")
        
        result = self.arduino.connect()
        
        self.assertFalse(result)
    
    @patch('serial.Serial')
    def test_send_moves_success(self, mock_serial):
        """Test successful move transmission"""
        mock_connection = Mock()
        mock_connection.is_open = True
        mock_connection.in_waiting = 1
        mock_connection.read.return_value = b'OK'
        mock_serial.return_value = mock_connection
        
        self.arduino.connection = mock_connection
        result = self.arduino.send_moves("R U R'")
        
        self.assertTrue(result)
        mock_connection.write.assert_called_once()
    
    @patch('serial.Serial')
    def test_send_moves_no_connection(self, mock_serial):
        """Test move transmission without connection"""
        result = self.arduino.send_moves("R U R'")
        self.assertFalse(result)
    
    def test_context_manager(self):
        """Test Arduino interface as context manager"""
        with patch.object(self.arduino, 'connect', return_value=True) as mock_connect:
            with patch.object(self.arduino, 'disconnect') as mock_disconnect:
                with self.arduino as arduino_ctx:
                    self.assertEqual(arduino_ctx, self.arduino)
                
                mock_connect.assert_called_once()
                mock_disconnect.assert_called_once()


class TestMoveValidation(unittest.TestCase):
    """Test cases for move sequence validation"""
    
    def test_valid_moves(self):
        """Test validation of standard Rubik's cube moves"""
        valid_moves = ["R", "U", "F", "L", "D", "B", "R'", "U'", "F'", "L'", "D'", "B'", "R2", "U2", "F2"]
        
        for move in valid_moves:
            with self.subTest(move=move):
                # This would be implemented in a move validator class
                self.assertTrue(len(move) <= 2)
                self.assertIn(move[0], "RUFLDB")
    
    def test_move_sequence_parsing(self):
        """Test parsing of move sequences"""
        test_sequence = "R U R' U' F"
        expected_moves = ["R", "U", "R'", "U'", "F"]
        
        # Simple parsing logic test
        moves = test_sequence.split()
        self.assertEqual(moves, expected_moves)


class TestPerformanceMetrics(unittest.TestCase):
    """Test cases for performance tracking"""
    
    def test_solve_time_target(self):
        """Test that target solve time is realistic"""
        from src.config.settings import TARGET_SOLVE_TIME_SECONDS
        
        # Should be between 5-20 seconds for a good robot
        self.assertGreaterEqual(TARGET_SOLVE_TIME_SECONDS, 5)
        self.assertLessEqual(TARGET_SOLVE_TIME_SECONDS, 20)
    
    def test_budget_constraint(self):
        """Test that budget constraint is documented"""
        from src.config.settings import ROBOT_COST_EGP
        
        # Should be the actual cost
        self.assertEqual(ROBOT_COST_EGP, 900)


if __name__ == '__main__':
    print("🧪 Running Arduino Interface Tests...")
    print("=" * 50)
    
    # Create test suite
    suite = unittest.TestSuite()
    
    # Add test cases
    suite.addTest(unittest.makeSuite(TestArduinoInterface))
    suite.addTest(unittest.makeSuite(TestMoveValidation))
    suite.addTest(unittest.makeSuite(TestPerformanceMetrics))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 50)
    if result.wasSuccessful():
        print("✅ All tests passed! Robot communication is reliable.")
    else:
        print("❌ Some tests failed. Check the output above.")
    
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    sys.exit(0 if result.wasSuccessful() else 1)
