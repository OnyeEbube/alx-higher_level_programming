#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1
    if count == 0:
        print("{:d} argument.\n".format(count))
    elif count == 1:
        print("{:d} argument:\n".format(count))
    else:
        print("{:d} arguments:\n".format(count))
    for i in range(1, len(sys.argv)):
        print("{}: {}\n".format(i, sys.argv[i]))
