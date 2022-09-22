#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 0:
        print("{:d} argument.".format(len(sys.argv)))
    elif len(sys.argv) == 1:
        print("{:d} argument:".format(len(sys.argv)))
    else:
        print("{:d} arguments:".format(len(sys.argv)))
    for i in range(0, len(sys.argv) + 1):
        print("{:d}: {:s}".format(i + 1, sys.argv[i]))
