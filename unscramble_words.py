#!/usr/bin/python

from __future__ import print_function
import sys, argparse

def main(argv):
    # Parsing inputs
    dict_file = ""
    scrambled_file = ""

    parser = argparse.ArgumentParser(description="Unscramble words from a string based on a given dictionary.")
    parser.add_argument("dict_file", metavar="dict_file", type=file, help="Dictionary file containing all words that should be considered for unscrambling.")
    parser.add_argument("scrambled_file", metavar="scrambled_file", type=argparse.FileType('w'), help="File containing the string with all words scrambled")

    args = parser.parse_args()

    print(args.length())

if __name__ == "__main__":
    main(sys.argv[1:])