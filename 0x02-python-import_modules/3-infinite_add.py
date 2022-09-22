#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
        add = 0
        for s in argv[1:]:
            if s != sys.argv[0]:
                add += int(s)
        print(add)
