# MergeIntervals
Docker usage:
docker build . -t mergeintervals
docker run -it --rm -v ${PWD}:/home/mergeintervals mergeintervals

Preconditions:
- python installed
    - download latest python 3.8 from https://www.python.org/downloads/
    - pip available via python e.g. python -m pip
- make installed
    - Windows:
        - download make from SourceForge: http://gnuwin32.sourceforge.net/packages/make.htm
        - install it
        - add install folder to PATH
    - Linux Ubuntu:
        sudo apt-get install build-essential

General idea merge:
- By sorting the intervals by their first value they can be merged in a constant way.
- After sorting, the first interval is put in the new merged list. 
- If the next interval in the list starts after the second value we treat it as an new interval in the merged list. 
- This new value will be compared against the next intervals of the sorted list.
- If the first value of the next interval overlaps with the one from the sorted list they can be merged.
- Multiple intervals with the same range e.g. [25,30],[25,30],[25,30] will also be merged since the first value is in the range of the previuos interval.

General idea unit-test:
- Since we only have one module and one function in that module unit testing is quite simple.
- First the basic functionality should be tested.
- Then error cases like wrong input or no input.

General idea performance-test:
- Space is constant additional space since we are sorting them in place, not copying them to a separte list. This halves memory used on runtime.
- For runtime the scanning is simple linear. The runtime of the sorting is depending on the sort algorithm used.

Time worked: approx. 5h

Build:
- Call "make init"
- Then "make build"

Unit-Test:
- Run "make unit-test"

Performance-Test:
- Run "make performance-test"

Cleanup:
- Run "make clean"

Installing the package:
- After building the package from the earlier step it can be installed with "python -m pip install dist/merge_pkg_AnSchwarzkopf-0.0.1-py3-none-any.whl"
- Uninstalling with "python -m pip uninstall dist/merge_pkg_AnSchwarzkopf-0.0.1-py3-none-any.whl"

A short demo with example intervals can be started with the following command "python demo/demo.py"
