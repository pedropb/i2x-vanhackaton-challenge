#!/usr/bin/python

from __future__ import print_function
import sys, argparse, re

def process_text(text_file):
    """Process input text file and return a list of unique words sorted by descending word length"""

    text = text_file.read().lower()
    text = re.sub(r"[^a-zA-Z ]", "", text)
    unique_words = list(set(text.split(" ")))
    unique_words.sort(key=lambda word: len(word), reverse=True)

    return unique_words

def unscramble(scrambled_file, word_vocab):
    """Unscramble scrambled_file using word_vocab. Words that weren't matched will be written in uppercase."""

    scrambled = scrambled_file.read().upper()
    for word in word_vocab:
        scrambled.replace(word.upper(), " " + word + " ")
    
    unscrambled = scrambled.trim()

    return unscrambled

def accuracy(text):
    return sum(1 for c in text if c.isupper())

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