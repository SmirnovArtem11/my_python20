import unittest
class CalcTests(unittest.TestCase):
    def test_pow(self):
        self.assertEqual(pow(1, 2), 3)
        
    def test_sum(self):
        self.assertEqual(sum([4, 2]), 6)
        
    def test_max(self):
        self.assertEqual(max(2, 5), 5)
        
    def test_min(self):
        self.assertEqual(min(8, 4), 4)

if __name__ == '__main__':
    unittest.main()