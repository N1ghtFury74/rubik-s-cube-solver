#!/usr/bin/env python3
"""
Rubik's Cube Solver Robot - Main Application Entry Point
Professional robotic solution by Momentum Software Team

This is the brain of the Rubik's cube solving robot that communicates
with Arduino hardware to achieve 10-12 second solve times.

Built with a 900 EGP budget in 2022.
"""

import logging
import sys
import os

# Add src to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.gui.cube_input_gui import CubeInputGUI
from src.config.settings import TARGET_SOLVE_TIME_SECONDS, ROBOT_COST_EGP, YEAR_BUILT


def setup_logging():
    """Configure logging for the application"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('logs/cube_solver.log'),
            logging.StreamHandler(sys.stdout)
        ]
    )


def main():
    """Main application entry point"""
    # Create logs directory if it doesn't exist
    os.makedirs('logs', exist_ok=True)
    
    # Setup logging
    setup_logging()
    logger = logging.getLogger(__name__)
    
    # Log startup information
    logger.info("=" * 60)
    logger.info("🤖 RUBIK'S CUBE SOLVER ROBOT STARTING")
    logger.info("=" * 60)
    logger.info(f"💰 Budget: {ROBOT_COST_EGP} EGP ({YEAR_BUILT})")
    logger.info(f"⚡ Target Solve Time: {TARGET_SOLVE_TIME_SECONDS} seconds")
    logger.info(f"🧠 Algorithm: Kociemba (Optimal)")
    logger.info(f"🔧 Hardware: 6 Stepper Motors + Arduino")
    logger.info("=" * 60)
    
    try:
        # Initialize and run the GUI application
        app = CubeInputGUI()
        logger.info("🚀 GUI initialized successfully")
        app.run()
        
    except KeyboardInterrupt:
        logger.info("👋 Application terminated by user")
    except Exception as e:
        logger.error(f"💥 Application error: {e}")
        sys.exit(1)
    finally:
        logger.info("🔚 Application shutdown complete")


if __name__ == "__main__":
    main()
