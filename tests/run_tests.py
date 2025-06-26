#!/usr/bin/env python3
"""
Test runner for gen-api-docs tests
"""

import os
import sys
import unittest
import argparse


def run_tests(test_pattern="test_*.py"):
    """Run all tests matching the pattern"""
    # Add the current directory to the path
    sys.path.insert(0, os.path.dirname(__file__))

    # Discover and run tests
    loader = unittest.TestLoader()
    suite = loader.discover(os.path.dirname(__file__), pattern=test_pattern)

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    return result.wasSuccessful()


def main():
    parser = argparse.ArgumentParser(description='Run gen-api-docs tests')
    parser.add_argument('--pattern', default='test_*.py',
                        help='Test file pattern (default: test_*.py)')
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='Verbose output')

    args = parser.parse_args()

    print("Running gen-api-docs tests...")
    print(f"Test pattern: {args.pattern}")
    print("=" * 50)

    success = run_tests(args.pattern)

    print("=" * 50)
    if success:
        print("✅ All tests passed!")
        sys.exit(0)
    else:
        print("❌ Some tests failed!")
        sys.exit(1)


if __name__ == '__main__':
    main()
