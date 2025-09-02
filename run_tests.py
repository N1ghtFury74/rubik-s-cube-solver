#!/usr/bin/env python3
"""
Test runner for the Rubik's Cube Solver Robot
Ensures 100% reliability before deployment
"""

import unittest
import sys
import os

# Add src to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def run_all_tests():
    """Run all test suites and provide comprehensive report"""
    print("🧪 RUBIK'S CUBE SOLVER - TEST SUITE")
    print("=" * 50)
    print("🎯 Ensuring 100% reliability for 10-12 second solve times")
    print("💰 Validating 900 EGP robot performance")
    print("=" * 50)
    
    # Discover and run all tests
    loader = unittest.TestLoader()
    start_dir = 'tests'
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    # Run tests with detailed output
    runner = unittest.TextTestRunner(
        verbosity=2,
        stream=sys.stdout,
        descriptions=True,
        failfast=False
    )
    
    result = runner.run(suite)
    
    # Print comprehensive summary
    print("\n" + "=" * 50)
    print("📊 TEST RESULTS SUMMARY")
    print("=" * 50)
    
    if result.wasSuccessful():
        print("✅ ALL TESTS PASSED!")
        print("🤖 Robot is ready for reliable cube solving")
        print("⚡ Expected performance: 10-12 second solve times")
    else:
        print("❌ SOME TESTS FAILED!")
        print("🔧 Please fix issues before deploying to robot")
    
    print(f"\n📈 Statistics:")
    print(f"   Tests Run: {result.testsRun}")
    print(f"   Failures: {len(result.failures)}")
    print(f"   Errors: {len(result.errors)}")
    print(f"   Success Rate: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%")
    
    if result.failures:
        print(f"\n💥 Failures:")
        for test, traceback in result.failures:
            print(f"   - {test}")
    
    if result.errors:
        print(f"\n🚨 Errors:")
        for test, traceback in result.errors:
            print(f"   - {test}")
    
    print("\n" + "=" * 50)
    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
