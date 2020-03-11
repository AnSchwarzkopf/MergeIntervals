# standard library
# https://medium.com/survata-engineering-blog/monitoring-memory-usage-of-a-running-python-program-49f027e3d1ba
import tracemalloc
import random
import sys
import os
# https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
import time

# custom library
sys.path.append(os.path.join("."))
from merge import merge

# Assumption: for the content those "performance" tests should be enough. Usually a framework should be used.

# creating function to simulate different inputs. for now assumption is, that 100 is the highest value possible in an interval
def createRandomIntegerList(amount: int):
    
    randomIntegerList = []

    for interval in range(0,amount):
        tempList = []
        firstValue = random.randint(0,100) 
        secondValue = random.randint(firstValue,100)
        tempList = [firstValue, secondValue]
        randomIntegerList.append(tempList)
    
    return randomIntegerList

''' All "performance" tests are made the same:
first getting the time the test was started.
then giving information which test it is.
Random intervals lists are created for different inputs (low, high, huge)
The memory check is started before the actual function.
Then output the used memory and time.
'''

def test_Performance_LowInput():
    start_time = time.time()
    print("Performance test Low input")
    randomizedList = createRandomIntegerList(4)
    tracemalloc.start()
    merge.mergeIntervals(randomizedList)
    current, peak = tracemalloc.get_traced_memory()
    print("Memory usage: %s MB" % (peak / 10**6))
    tracemalloc.stop()
    print("--- %s seconds ---" % (time.time() - start_time))

def test_Performance_LargeInput():
    start_time = time.time()
    print("Performance test large input")
    randomizedList = createRandomIntegerList(50000)
    tracemalloc.start()
    merge.mergeIntervals(randomizedList)
    current, peak = tracemalloc.get_traced_memory()
    print("Memory usage: %s MB" % (peak / 10**6))
    tracemalloc.stop()
    print("--- %s seconds ---" % (time.time() - start_time))

def test_Performance_HugeInput():
    start_time = time.time()
    print("Performance test huge input")
    randomizedList = createRandomIntegerList(500000)
    tracemalloc.start()
    merge.mergeIntervals(randomizedList)
    current, peak = tracemalloc.get_traced_memory()
    print("Memory usage: %s MB" % (peak / 10**6))
    tracemalloc.stop()
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    test_Performance_LowInput()
    test_Performance_LargeInput()
    test_Performance_HugeInput()