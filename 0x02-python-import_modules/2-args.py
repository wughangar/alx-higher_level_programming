#!/usr/bin/python3
import sys
if __name__ == "__main__":
    def main():
        argc = len(sys.argv) - 1
        argv = sys.argv[1:]
        print("{} argument(s):".format(argc))
        if argc == 0:
            print(".")
        else:
            for i, j in enumerate(argv, start=1):
                print("{}: {}".format(i, j))
main()
