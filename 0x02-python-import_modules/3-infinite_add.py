#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv)
    args = sys.argv
    sum = 0
    if count == 1:
        print("{}".format(0))
    else:
        for i in range(1, (count)):
            sum += int(args[i])
        print("{}".format(sum))
