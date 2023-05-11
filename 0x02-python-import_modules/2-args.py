#!/usr/bin/python3
import sys
if __name__ == "__main__":
    def main():
        argc = len(sys.argv)
        argv = sys.argv

        if argc == 1:
            print(".")
        else:
            for i in range(argc):
                print("{}: {}".format(i, argv[i]))

