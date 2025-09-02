#!/usr/bin/env python3
"""
Setup script for the Rubik's Cube Solver Robot
Professional installation and configuration
"""

import os
import sys
import subprocess
import platform

def check_python_version():
    """Ensure Python 3.7+ is being used"""
    if sys.version_info < (3, 7):
        print("❌ Error: Python 3.7 or higher is required")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    print(f"✅ Python version: {sys.version.split()[0]}")

def install_dependencies():
    """Install required Python packages"""
    print("📦 Installing Python dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully")
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        sys.exit(1)

def create_directories():
    """Create necessary directories"""
    directories = ['logs', 'docs', 'tests']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"📁 Created directory: {directory}")

def check_arduino_ide():
    """Check if Arduino IDE is available"""
    print("🔍 Checking for Arduino IDE...")
    
    # Common Arduino IDE paths
    arduino_paths = [
        "C:\\Program Files (x86)\\Arduino\\arduino.exe",
        "C:\\Program Files\\Arduino\\arduino.exe",
        "/Applications/Arduino.app",
        "/usr/bin/arduino"
    ]
    
    arduino_found = False
    for path in arduino_paths:
        if os.path.exists(path):
            print(f"✅ Arduino IDE found: {path}")
            arduino_found = True
            break
    
    if not arduino_found:
        print("⚠️  Arduino IDE not found in common locations")
        print("   Please install Arduino IDE manually from: https://www.arduino.cc/en/software")

def display_next_steps():
    """Display setup completion and next steps"""
    print("\n" + "🎉" + "=" * 48 + "🎉")
    print("   RUBIK'S CUBE SOLVER SETUP COMPLETE!")
    print("=" * 50)
    print("\n📋 Next Steps:")
    print("1. 🔌 Connect your Arduino to the computer")
    print("2. 📤 Upload arduino/rubiks_cube_controller/rubiks_cube_controller.ino")
    print("3. ⚙️  Update COM port in src/config/settings.py")
    print("4. 🧪 Run tests: python run_tests.py")
    print("5. 🚀 Launch application: python main.py")
    print("\n🎯 Expected Performance:")
    print("   • Solve Time: 10-12 seconds")
    print("   • Budget: 900 EGP total cost")
    print("   • Reliability: 100% success rate")
    print("\n🎥 Demo Video: https://www.facebook.com/MomentumTeamMU/videos/275886227754531/")
    print("\n🤖 Happy cube solving! - Momentum Team")

def main():
    """Main setup function"""
    print("🤖 RUBIK'S CUBE SOLVER ROBOT - SETUP")
    print("=" * 40)
    print("💰 900 EGP Budget Solution")
    print("⚡ 10-12 Second Solve Times")
    print("🧠 Kociemba Algorithm Brain")
    print("=" * 40)
    
    # Run setup steps
    check_python_version()
    create_directories()
    install_dependencies()
    check_arduino_ide()
    display_next_steps()

if __name__ == "__main__":
    main()
