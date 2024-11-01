import unittest
from fibonacci import fibonacci3

class TestFibonacci(unittest.TestCase):
    def test_fibonacci3_base_cases(self):
        self.assertEqual(fibonacci3(0), 1)
        self.assertEqual(fibonacci3(1), 1)
        self.assertEqual(fibonacci3(2), 1)

    def test_fibonacci3_recursive_cases(self):
        self.assertEqual(fibonacci3(3), 2)
        self.assertEqual(fibonacci3(4), 3)
        self.assertEqual(fibonacci3(5), 5)
        self.assertEqual(fibonacci3(10), 55)
        self.assertEqual(fibonacci3(20), 6765)

    def test_fibonacci3_large_input(self):
        self.assertEqual(fibonacci3(50), 12586269025)

if __name__ == "__main__":
    unittest.main()