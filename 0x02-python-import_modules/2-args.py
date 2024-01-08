#!/usr/bin/python3
import sys
count = len(sys.argv)
args = sys.argv
index = count - 1
if count == 1:
    print("{} arguments.".format(index))
elif count == 2:
    print("{} argument:".format(index))
    print("{}: {}.".format(index, args[index]))
else:
    print("{} arguments:".format(index))
    for i in range(1, count):
        print("{}: {}.".format(i, args[i]))
