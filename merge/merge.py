# @Andreas Schwarzkopf (schwarzkopf.and@gmail.com)

# standard library

# third party

# example input [25,30] [2,19] [14,23] [4,8]

def mergeIntervals(intervals: list) -> list:
    mergedIntervals = []

    # raise TypeError if intervals is not list
    if not isinstance(intervals, list):
        raise TypeError

    # return empty list if no interval is given
    if not intervals:
        return mergedIntervals

    # sort intervals by the first key source : https://stackoverflow.com/questions/21068315/python-sort-first-element-of-list
    sortedIntervals = sorted(intervals, key=lambda x: x[0])
    print(sortedIntervals)

    for interval in sortedIntervals:
        # add interval to mergedIntervals if interval does not overlap with previous 
        # or mergedIntervals is empty e.g. for the first interval
        if not mergedIntervals or mergedIntervals[-1][1] < interval[0]:
            mergedIntervals.append(interval)
        else:
            # in the other case there is overlap so merge previous interval with current one
            mergedIntervals[-1][1] = max(mergedIntervals[-1][1], interval[1])

    return mergedIntervals