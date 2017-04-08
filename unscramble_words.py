#!/usr/bin/python

from __future__ import print_function
import sys, argparse, re
from os.path import isfile
from numpy import random

def process_text(dict_file):
    """Process 'dict_file' and return a list of unique words sorted by descending word length"""

    text = dict_file.lower()
    text = re.sub(r"[^a-zA-Z ]", "", text)
    unique_words = list(set(text.split(" ")))
    unique_words.sort(key=lambda word: len(word), reverse=True)

    return unique_words

def drop_words(word_vocab, n=3):
    """Drop n words from 'word_vocab' to simulate unknown words."""

    dropped_words = random.choice([w for w in word_vocab if len(w) >= 3], n, replace=False)
    dropped_vocab = [w for w in word_vocab if w not in dropped_words]
    return dropped_vocab, dropped_words


def unscramble(scrambled_file, word_vocab):
    """Unscramble 'scrambled_file' using 'word_vocab'. Words that weren't matched will be written in uppercase."""

    scrambled = scrambled_file.upper()
    for word in word_vocab:
        scrambled = scrambled.replace(word.upper(), " " + word + " ")
    
    unscrambled = scrambled.strip()

    return unscrambled

def accuracy(text):
    """Returns the number of unrecognized characters"""
    return sum(1 for c in text if c.isupper())

def main(argv):

    # Configuring arguments    
    parser = argparse.ArgumentParser(
        description=(
            "Unscramble words from a string based on a given dictionary. Words not present on "
            "the dictionary will be written in UPPERCASE on the output and will count towards "
            "the number of unrecognized characters." 
        )
    )

    parser.add_argument("dict_file", metavar="dict_file", type=str, 
        help="A text file containing all words that should be considered for unscrambling.")

    parser.add_argument("scrambled_file", metavar="scrambled_file", type=str, 
        help="File containing the string with all words scrambled")

    parser.add_argument("-d", "--drop", dest="drop", metavar="n", type=int, default=3,
        help="Number of random words to drop from dictionary, before scrambling")

    parser.add_argument("-v", "--verbose", dest="verbose", action="store_true", default=False, 
        help="Verbose output", required=False)

    # Parsing arguments
    args = parser.parse_args()

    # Print help and exit if there are not enough arguments
    if len(argv) < 2:
        parser.print_help()
        sys.exit(1)

    try:
        # Optional arguments
        verbose = args.verbose
        drop = args.drop

        # Checking if input files exist
        if not isfile(args.dict_file):
            print("Invalid argument: dict_file == " + args.dict_file)
            return
        
        if not isfile(args.scrambled_file):
            print("Invalid argument: scrambled_file == " + args.scrambled_file)
            return
        
        # Reading files
        dict_file_text = ""
        with open(args.dict_file) as f:
            dict_file_text = f.read()

        # Error handling
        if len(dict_file_text.strip()) == 0:
            print("dict_file is empty.")
        
        scrambled_file_text = ""
        with open(args.scrambled_file) as f:
            scrambled_file_text = f.read()

        if len(scrambled_file_text.strip()) == 0:
            print("scrambled_file is empty.")
              
        # Creating word vocabulary
        word_vocab = process_text(dict_file_text)

        # Optionally, removing words from dictionary 
        if drop > 0:
            word_vocab, dropped_words = drop_words(word_vocab, n=drop)

        # Unscrambling input
        unscrambled_text = unscramble(scrambled_file_text, word_vocab)

        # Verbose output
        if verbose:
            print("Scrambled text:", scrambled_file_text)
            print("Dictionary:", word_vocab)
            print("Words dropped from Dictionary:", dropped_words)

        # Final output
        print("Unscrambled text:", unscrambled_text)
        print("Unrecognized characters: ", accuracy(unscrambled_text))

    except IOError as err:
        print(err.filename, err.message)
    except ValueError as err:
        print(err.message)
    except:
        print("Unexpected error")



if __name__ == "__main__":
    main(sys.argv[1:])