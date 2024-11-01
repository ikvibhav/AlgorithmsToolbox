import unittest
from canSum import can_sum_memo

class TestCanSum(unittest.TestCase):

    def test_can_sum_memo(self):
        self.assertTrue(can_sum_memo(7, [2, 3], {}))
        self.assertTrue(can_sum_memo(7, [5, 3, 4, 7], {}))
        self.assertTrue(can_sum_memo(8, [2, 3, 5], {}))
        self.assertFalse(can_sum_memo(7, [2, 4], {}))
        self.assertFalse(can_sum_memo(300, [7, 14], {}))

if __name__ == "__main__":
    unittest.main()