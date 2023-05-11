#!/usr/bin/python3
import sys

if __name__ == "__main__":
    apassed = sys.argv[1:]
    total = sum(int(i) for i in apassed)
    print(total)
