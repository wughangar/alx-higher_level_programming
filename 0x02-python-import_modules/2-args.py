#!/usr/bin/python3
import sys
if __name__ == "__main__":
    def main():
        argc = len(sys.argv) - 1
        argv = sys.argv[1:]
        if argc == 1:
            print("{} argument:".format(argc))
        elif argc == 0:
            print(" 0 arguments. \n .")
        else:
            print("{} arguments:".format(argc))

        for i, j in enumerate(argv, start=1):
                print("{}: {}".format(i, j))
main()
