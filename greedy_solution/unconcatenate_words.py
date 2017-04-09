#!/usr/bin/python

from __future__ import print_function
import sys, argparse, os
sys.path.append('../dataset_tools')
import dataset_tools
from collections import Counter
from six.moves import cPickle as pickle

def process_dict(text, frequency_threshold):
    """
    Process 'text' and return a list of unique words sorted by descending word length.
    During processing, we remove single letters words (1 char). We also remove uncommon 
    words (<1% occurrence).

    Our dictionary is composed by the text8 dataset (http://mattmahoney.net/dc/textdata).

    This dataset contains the first 10^9 bytes of the English Wikipedia dump on Mar. 3, 2006.

    This dataset is cleaned and only contains lowercase characters from a to z, plus whitespace.
    """

    # Trying to load previous unique_words (pickle file)
    UNIQUE_WORDS_PICKLE = "unique_words_with_frequency_" + str(frequency_threshold) + ".pickle"
    
    unique_words = None
    if os.path.isfile(UNIQUE_WORDS_PICKLE):
        try:
            with open(UNIQUE_WORDS_PICKLE, 'r') as f:
                unique_words = pickle.load(f)
        except:
            os.remove(UNIQUE_WORDS_PICKLE)
            unique_words = None

    if (type(unique_words) == list):
        return unique_words


    WORD_COUNT_PICKLE = "word_count.pickle"
    WORD_COUNT = 253855

    print("Processing dictionary. This will take a while.")

    # Trying to load previous word_count (pickle file)
    word_count = None
    if os.path.isfile(WORD_COUNT_PICKLE):
        try:
            with open(WORD_COUNT_PICKLE, 'r') as f:
                word_count = pickle.load(f)
            if len(word_count) != WORD_COUNT:
                os.remove(WORD_COUNT_PICKLE)
                word_count = None
        except:
            raise
            os.remove(WORD_COUNT_PICKLE)
            word_count = None

    # count words
    if word_count == None:
        print("Pickle file not found. Counting word occurence...")

        # grab all the words
        words = text.split(" ")

        # counting word occurence
        word_count = dict(Counter(words).most_common())
    
        # saving word count for future reuse
        with open(WORD_COUNT_PICKLE, 'w') as f:
            pickle.dump(word_count, f)
            print("Word count saved for future reuse.")
    
    # making sure we have the correct count loaded
    assert(type(word_count) == dict)
    assert(len(word_count) == WORD_COUNT)

    # remove the duplicates and single-character words.
    unique_words = [w for w in word_count.keys() if len(w) > 1]
    vocab_size = len(unique_words)
    print("Vocab size:", vocab_size)

    # remove words with frequency lower than 1%
    unique_words = [word for word in unique_words if float(word_count[word]) / vocab_size > frequency_threshold]
    print("Vocab size (>%.3f%% frequency): %d" % ((frequency_threshold * 100), len(unique_words)))

    unique_words.sort(key=lambda word: len(word), reverse=True)
    unique_words.append('a')
    unique_words.append('i')

    # save unique words for future reuse
    with open(UNIQUE_WORDS_PICKLE, 'w') as f:
        pickle.dump(unique_words, f)
        print("unique_words saved for future reuse.")

    return unique_words

def unconcatenate(concatenated_file, word_vocab):
    """Unconcatenate 'concatenated_file' using 'word_vocab'. Words that weren't matched will be written in uppercase."""

    concatenated = concatenated_file.upper()
    for word in word_vocab:
        concatenated = concatenated.replace(word.upper(), " " + word + " ")
    
    unconcatenated = concatenated.strip()

    return unconcatenated

def accuracy(text):
    """Returns the number of unrecognized characters"""
    return sum(1 for c in text if c.isupper())

def main(argv):
    # Configuring arguments    
    parser = argparse.ArgumentParser(
        description=(
            "Unconcatenate words from a string based on a given dictionary. Words not present on "
            "the dictionary will be written in UPPERCASE on the output and will count towards "
            "the number of unrecognized characters. Outputs: the unconcatenated string and the "
            "number of unrecongized characters." 
        )
    )

    parser.add_argument("concatenated_file", metavar="concatenated_file", type=str, 
        help="File containing the string with all words concatenated")

    parser.add_argument("-t", "--frequency-threshold", dest="frequency_threshold", type=float, default=0.001, 
        help=(
            "Frequency threshold (in %%) for considering words from the corpus dictionary (Default: 0.001)."
            " For example, words that appear on the corpus dictionary less than 0.001%% won't be used."
        ), required=False)

    # Parsing arguments
    args = parser.parse_args()

    # Print help and exit if there are not enough arguments
    if len(argv) < 1:
        parser.print_help()
        sys.exit(1)

    try:
        # Threshold argument
        threshold = args.frequency_threshold / 100
        if (threshold > 1 or threshold <= 0):
            print("Invalid argument: frequency threshold. Expected float between 100 and 0 (not inclusive).")

        # Download DICT FILE
        dict_file = dataset_tools.maybe_download()

        # Checking if input files exist
        if not os.path.isfile(dict_file):
            print("Dictionary file missing: " + dict_file)
            return
        
        if not os.path.isfile(args.concatenated_file):
            print("Invalid argument: concatenated_file == " + args.concatenated_file)
            return
        
        # Reading files
        dict_file_text = dataset_tools.read_dict_file(dict_file)

        # Error handling
        if len(dict_file_text.strip()) == 0:
            print("dict_file is empty.")
        
        concatenated_file_text = ""
        with open(args.concatenated_file) as f:
            concatenated_file_text = f.read()

        if len(concatenated_file_text.strip()) == 0:
            print("concatenated_file is empty.")
              
        # Creating word vocabulary
        word_vocab = process_dict(dict_file_text, frequency_threshold=threshold)

        # Unconcatenating input
        unconcatenated_text = unconcatenate(concatenated_file_text, word_vocab)

        # Final output
        print("Concatenated text:", concatenated_file_text)
        print("Unconcatenated text:", unconcatenated_text)
        print("Unrecognized characters: ", accuracy(unconcatenated_text))

    except IOError as err:
        print(err.filename, err.message)
    except ValueError as err:
        print(err.message)
    except:
        raise
        print("Unexpected error")



if __name__ == "__main__":
    main(sys.argv[1:])