#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1
    sum = 0
    for i in (1, count):
        sum = sum + sys.argv[i + 1]
        print("{}".format(sum))
