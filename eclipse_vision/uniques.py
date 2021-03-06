# Adam Vilmin
# Illinois State Geological Survey, University of Illinois
# 2015-05-31

from collections import defaultdict
from sys import argv


def uniques(rf, wf):
    """script for finding searchable values in PRT file"""
    types = defaultdict(int)

    for line in rf:
        line = line.strip()
        if line != "":
            types[line] += 1

    for key, value in types.items():
        wf.write('"' + key + '"' + " occurs " + str(value) + " times.\n")

if __name__ == '__main__':

    rf = open(argv[1], 'r')
    wf = open(argv[2], 'w')

    uniques(rf, wf)
