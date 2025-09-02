#!/usr/bin/env python3
"""
Project Structure Validation Script
Ensures the Rubik's Cube Solver Robot project is properly organized
"""

import os
import sys

def validate_structure():
    """Validate that all required files and directories are in place"""
    print("🔍 VALIDATING PROJECT STRUCTURE")
    print("=" * 50)
    
    # Required directories
    required_dirs = [
        'src',
        'src/config',
        'src/core', 
        'src/gui',
        'src/communication',
        'arduino',
        'arduino/rubiks_cube_controller',
        'tests',
        'docs',
        'docs/resources',
        'legacy',
        'media',
        'logs'
    ]
    
    # Required files
    required_files = [
        'main.py',
        'setup.py',
        'run_tests.py',
        'requirements.txt',
        'README.md',
        'CHANGELOG.md',
        'QUICK_START.md',
        'PROJECT_STRUCTURE.md',
        'src/__init__.py',
        'src/config/__init__.py',
        'src/config/settings.py',
        'src/core/__init__.py',
        'src/core/cube_solver.py',
        'src/gui/__init__.py',
        'src/gui/cube_input_gui.py',
        'src/communication/__init__.py',
        'src/communication/arduino_interface.py',
        'arduino/rubiks_cube_controller/rubiks_cube_controller.ino',
        'tests/__init__.py',
        'tests/test_cube_solver.py',
        'tests/test_arduino_interface.py',
        'docs/API_REFERENCE.md',
        'docs/HARDWARE_SETUP.md',
        'docs/PERFORMANCE_ANALYSIS.md',
        'legacy/README_ORIGINAL.md'
    ]
    
    # Check directories
    print("📁 Checking directories...")
    missing_dirs = []
    for directory in required_dirs:
        if os.path.exists(directory):
            print(f"   ✅ {directory}")
        else:
            print(f"   ❌ {directory}")
            missing_dirs.append(directory)
    
    # Check files
    print("\n📄 Checking files...")
    missing_files = []
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"   ✅ {file_path}")
        else:
            print(f"   ❌ {file_path}")
            missing_files.append(file_path)
    
    # Check for unwanted files in root
    print("\n🧹 Checking for unwanted files in root...")
    root_files = [f for f in os.listdir('.') if os.path.isfile(f)]
    allowed_root_files = [
        'main.py', 'setup.py', 'run_tests.py', 'requirements.txt',
        'README.md', 'CHANGELOG.md', 'QUICK_START.md', 'PROJECT_STRUCTURE.md',
        'validate_structure.py', '.gitignore'
    ]
    
    unwanted_files = [f for f in root_files if f not in allowed_root_files]
    
    if unwanted_files:
        print("   ⚠️  Unwanted files found:")
        for file in unwanted_files:
            print(f"      - {file}")
    else:
        print("   ✅ No unwanted files in root")
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 VALIDATION SUMMARY")
    print("=" * 50)
    
    total_dirs = len(required_dirs)
    total_files = len(required_files)
    
    if not missing_dirs and not missing_files and not unwanted_files:
        print("🎉 PROJECT STRUCTURE IS PERFECT!")
        print("✅ All required directories present")
        print("✅ All required files present") 
        print("✅ No unwanted files in root")
        print("\n🤖 Your robot is ready for professional deployment!")
        return True
    else:
        print("⚠️  PROJECT STRUCTURE NEEDS ATTENTION:")
        if missing_dirs:
            print(f"   📁 Missing directories: {len(missing_dirs)}")
        if missing_files:
            print(f"   📄 Missing files: {len(missing_files)}")
        if unwanted_files:
            print(f"   🧹 Unwanted files: {len(unwanted_files)}")
        return False

def display_structure_tree():
    """Display the current project structure as a tree"""
    print("\n🌳 CURRENT PROJECT TREE")
    print("=" * 30)
    
    for root, dirs, files in os.walk('.'):
        # Skip hidden directories and __pycache__
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        
        level = root.replace('.', '').count(os.sep)
        indent = ' ' * 2 * level
        print(f'{indent}📁 {os.path.basename(root)}/')
        
        subindent = ' ' * 2 * (level + 1)
        for file in files:
            if not file.startswith('.') and not file.endswith('.pyc'):
                if file.endswith('.py'):
                    print(f'{subindent}🐍 {file}')
                elif file.endswith('.ino'):
                    print(f'{subindent}🤖 {file}')
                elif file.endswith('.md'):
                    print(f'{subindent}📚 {file}')
                elif file.endswith(('.mkv', '.mp4', '.avi')):
                    print(f'{subindent}🎥 {file}')
                elif file.endswith(('.jpg', '.png', '.gif')):
                    print(f'{subindent}🖼️  {file}')
                else:
                    print(f'{subindent}📄 {file}')

if __name__ == "__main__":
    print("🤖 RUBIK'S CUBE SOLVER - STRUCTURE VALIDATOR")
    print("💰 900 EGP Robot - Professional Organization")
    print("⚡ 10-12 Second Solve Times")
    
    # Validate structure
    is_valid = validate_structure()
    
    # Display tree
    display_structure_tree()
    
    # Exit with appropriate code
    sys.exit(0 if is_valid else 1)
