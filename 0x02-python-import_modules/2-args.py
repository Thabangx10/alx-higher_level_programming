#!/usr/bin/python3

if __name__ == "__main__":
    """Printing the num of lists as arguments with the use of len(argv)."""
    import sys
    argv = sys.argv[1:]
    count = len(argv)
    index = 1
    if count == 0:
        print("{:d} arguments.". format(count))
    elif count == 1:
        print("{:d} argument:". format(count))
        print("{:d}: {:s}". format(index, sys.argv[1:]))
    else:
        print("{:d} arguments:". format(count))
    """using the while loop to iterate through the count variable"""
    while index <= count:
        print("{:d}: {:s}". format(index, sys.argv[index]))
        index += 1
