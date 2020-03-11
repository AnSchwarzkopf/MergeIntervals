# standard library
import unittest

# custom library
from merge import merge

class TestMerge(unittest.TestCase):

    # test basic functionality
    def test_mergeIntervals_Function(self):
        self.assertEqual(merge.mergeIntervals([[25,30],[2,19],[14,23],[4,8]]), [[2,23],[25,30]])
    
    # test empty lists
    def test_mergeIntervals_OnEmptyList(self):
        self.assertEqual(merge.mergeIntervals([]), [])
    
    # test wrong input type top level
    def test_mergeIntervals_WrongInputTypeString(self):
        self.assertRaises(TypeError, merge.mergeIntervals, "")
    
    # test wrong input type low level
    def test_mergeIntervals_WrongInputTypeListOfStringsAndInteger(self):
        self.assertRaises(TypeError, merge.mergeIntervals, [["3","4"],[1,2]])

if __name__ == '__main__':
    unittest.main()