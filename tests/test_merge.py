import unittest
from merge import merge

class TestMerge(unittest.TestCase):

    def test_mergeIntervals_1(self):
        self.assertEqual(merge.mergeIntervals([[25,30],[2,19],[14,23],[4,8]]), [[2,23],[25,30]])
    
    def test_mergeIntervals_2(self):
        self.assertEqual(merge.mergeIntervals([]), [])
    
    def test_mergeIntervals_3(self):
        self.assertRaises(TypeError, merge.mergeIntervals, "")

if __name__ == '__main__':
    unittest.main()