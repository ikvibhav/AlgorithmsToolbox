import unittest
from gridTraveller import grid_traveller

class TestGridTraveller(unittest.TestCase):
    def test_1x1_grid(self):
        self.assertEqual(grid_traveller(1, 1), 1)

    def test_2x3_grid(self):
        self.assertEqual(grid_traveller(2, 3), 3)

    def test_3x2_grid(self):
        self.assertEqual(grid_traveller(3, 2), 3)

    def test_3x3_grid(self):
        self.assertEqual(grid_traveller(3, 3), 6)

    def test_0x0_grid(self):
        self.assertEqual(grid_traveller(0, 0), 0)

    def test_0x5_grid(self):
        self.assertEqual(grid_traveller(0, 5), 0)

    def test_5x0_grid(self):
        self.assertEqual(grid_traveller(5, 0), 0)

    def test_large_grid(self):
        self.assertEqual(grid_traveller(18, 18), 2333606220)

if __name__ == "__main__":
    unittest.main()