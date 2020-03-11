# @Andreas Schwarzkopf (schwarzkopf.and@gmail.com)

# standard library
# using List to handle duplicates and order of the intervals and to define input/output of function
from typing import List

# example input [[25,30],[2,19],[14,23],4,8]]

# Expected type for input and output are a List of Lists of Integers
# Assumption: Since this module is only used for this coding task and not with pandas etc. integer will not cause memory overflow
def mergeIntervals(intervals: List[List[int]]) -> List[List[int]]:
    mergedIntervals = []

    # Assumption: raise TypeError if intervals is not List
    if not isinstance(intervals, List):
        raise TypeError

    # Assumption: return empty list if no interval is given
    if not intervals:
        return []

    # sort intervals by the first key source : https://stackoverflow.com/questions/21068315/python-sort-first-element-of-list
    intervals.sort(key=lambda x: x[0])

    for interval in intervals:
        # add interval to mergedIntervals if interval does not overlap with previous 
        # or mergedIntervals is empty e.g. for the first interval
        if not mergedIntervals or mergedIntervals[-1][1] < interval[0]:
            mergedIntervals.append(interval)
        else:
            # in the other case there is overlap so merge previous interval with current one
            # https://www.programiz.com/python-programming/methods/built-in/max
            mergedIntervals[-1][1] = max(mergedIntervals[-1][1], interval[1])

    return mergedIntervals