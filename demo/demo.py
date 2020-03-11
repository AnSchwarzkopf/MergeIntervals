# standard library
import os
import sys

# custom library
sys.path.append(os.path.join("merge"))
import merge

if __name__ == "__main__":
    inputInterval = [[25,30],[2,19],[14,23],[4,8]]
    print("Input: %s" % inputInterval)
    OutputInterval = merge.mergeIntervals(inputInterval)
    print("Output: %s" % OutputInterval)