"""
Arduino Communication Interface
Handles serial communication with the Arduino controller
"""

import serial
import time
import logging
from typing import Optional
from ..config.settings import ARDUINO_PORT, ARDUINO_BAUDRATE, ARDUINO_TIMEOUT

logger = logging.getLogger(__name__)


class ArduinoInterface:
    """
    Professional Arduino communication interface for the Rubik's cube robot
    """
    
    def __init__(self, port: str = ARDUINO_PORT, baudrate: int = ARDUINO_BAUDRATE):
        self.port = port
        self.baudrate = baudrate
        self.timeout = ARDUINO_TIMEOUT
        self.connection: Optional[serial.Serial] = None
        
    def connect(self) -> bool:
        """
        Establish connection with Arduino
        
        Returns:
            True if connection successful, False otherwise
        """
        try:
            self.connection = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
            time.sleep(3)  # Allow Arduino to initialize
            logger.info(f"Connected to Arduino on {self.port} at {self.baudrate} baud")
            return True
        except serial.SerialException as e:
            logger.error(f"Failed to connect to Arduino: {e}")
            return False
    
    def disconnect(self) -> None:
        """Close the Arduino connection"""
        if self.connection and self.connection.is_open:
            self.connection.close()
            logger.info("Disconnected from Arduino")
    
    def send_moves(self, moves: str) -> bool:
        """
        Send solving moves to Arduino
        
        Args:
            moves: String of Rubik's cube moves (e.g., "R U R' U'")
            
        Returns:
            True if moves sent successfully, False otherwise
        """
        if not self.connection or not self.connection.is_open:
            logger.error("Arduino not connected")
            return False
        
        try:
            # Send moves to Arduino
            moves_bytes = moves.encode('utf-8')
            self.connection.write(moves_bytes)
            logger.info(f"Sent moves to Arduino: {moves}")
            
            # Wait for Arduino response
            self._wait_for_response()
            return True
            
        except Exception as e:
            logger.error(f"Failed to send moves to Arduino: {e}")
            return False
    
    def _wait_for_response(self) -> str:
        """
        Wait for and read Arduino response
        
        Returns:
            Response string from Arduino
        """
        response = ""
        
        # Wait for data to be available
        while self.connection.in_waiting == 0:
            time.sleep(0.1)
        
        time.sleep(1)  # Allow all data to arrive
        
        # Read all available data
        while self.connection.in_waiting > 0:
            try:
                byte_data = self.connection.read()
                response += byte_data.decode('utf-8', errors='ignore')
            except UnicodeDecodeError:
                logger.warning("Failed to decode Arduino response")
                
        logger.info(f"Arduino response: {response.strip()}")
        return response.strip()
    
    def send_test_command(self) -> bool:
        """
        Send a test command to verify Arduino communication
        
        Returns:
            True if test successful, False otherwise
        """
        return self.send_moves("U")  # Simple test move
    
    def emergency_stop(self) -> bool:
        """
        Send emergency stop command to Arduino
        
        Returns:
            True if stop command sent successfully
        """
        try:
            if self.connection and self.connection.is_open:
                self.connection.write(b"STOP")
                logger.info("Emergency stop command sent")
                return True
        except Exception as e:
            logger.error(f"Failed to send emergency stop: {e}")
        return False
    
    def __enter__(self):
        """Context manager entry"""
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        self.disconnect()
