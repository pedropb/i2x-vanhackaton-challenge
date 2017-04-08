#!/usr/bin/python

from __future__ import print_function
import sys, argparse, re

def process_text(text_file):
    """Process input text file and return a list of unique words sorted by 
    descending word length"""

    text = text_file.read()
    text = re.sub(r"[^a-zA-Z ]", "", text)
    unique_words = list(set(text.split(" ")))
    unique_words.sort(key=lambda word: len(word), reverse=True)

    return unique_words

def process_scrambled(scrambled_file):
    # TODO: process the scrambled file, splitting the string in words
    # present on the dictionary. This should minimize the number of
    # unknown words

    return None

def main(argv):
    # Parsing inputs
    parser = argparse.ArgumentParser(
        description="Unscramble words from a string based on a given dictionary.")

    parser.add_argument("text_file", metavar="text_file", type=file, 
        help="A text file containing all words that should be considered for unscrambling.")

    parser.add_argument("scrambled_file", metavar="scrambled_file", type=argparse.FileType('w'), 
        help="File containing the string with all words scrambled")

    try:
        args = parser.parse_args()
        text_file = args.text_file
        scrambled_file = args.scrambled_file

        text = process_text(text_file)
        print(text)

    except IOError as err:
        print(err.strerror, "->", err.filename)
    except:
        err = sys.exc_info()
        print("Unexpected error:", err[1])



if __name__ == "__main__":
    main(sys.argv[1:])