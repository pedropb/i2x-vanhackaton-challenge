# i2x Vanhackaton challenge of 2017.

`unconcatenate_words.py` is a tool to unconcatenate strings (as "iwanttogotoberlin" -> "i want to go to berlin") using a given dictionary.

## Installation

```
$ git clone https://github.com/pedropb/i2x-challenge
```

## Usage

```
$ cd i2x-challenge
$ ./unconcatenate_words.py -h
usage: unconcatenate_words.py [-h] [-d n] [-v] dict_file scrambled_file

Unconcatenate words from a string based on a given dictionary. Words not present
on the dictionary will be written in UPPERCASE on the output and will count
towards the number of unrecognized characters.

positional arguments:
dict_file       A text file containing all words that should be considered
                for unscrambling.
scrambled_file  File containing the string with all words scrambled

optional arguments:
-h, --help      show this help message and exit
-d n, --drop n  Number of random words to drop from dictionary, before
                scrambling
-v, --verbose   Verbose output
```


## Examples

<details>
<summary>$ ./unconcatenate_words.py examples/dicts/text1 examples/concat/text1 -v</summary>
Concatenated text: YouhavejustcompletedalengthydocumentwhenyouhaveanunfortunateFindReplacemishapYouhaveaccidentallyremovedallspacespunctuationandcapitalisationinthedocument

Dictionary: ['capitalisation', 'accidentally', 'unfortunate', 'findreplace', 'punctuation', 'completed', 'document', 'lengthy', 'removed', 'mishap', 'spaces', 'have', 'all', 'you', 'the', 'in', 'an', 'a']

Words dropped from Dictionary: ['just' 'and' 'when']

Unconcatenated text: you  have JUST completed  a  lengthy  document WHEN you  have  an  unfortunate  findreplace  mishap  you  have  accidentally  removed  all  spaces  punctuation  an D capitalisation  in  the  document

Unrecognized characters:  9
</details>

<details>
<summary>$ ./unconcatenate_words.py examples/dicts/text2 examples/concat/text2 -v</summary>
Concatenated text: YoufigurethatyoucanaddbackinthepunctationandcapitalisationlateronceyougettheindividualwordsproperlyseparatedMostofthew
ordswillbeinadictionarybutsomestringslikepropernameswillnot

Dictionary: ['capitalisation', 'individual', 'dictionary', 'punctation', 'separated', 'strings', 'figure', 'proper', 'names', 'words', 'later', 'some', 'back', 'that', 'most', 'like', 'will', 'once', 'get', 'add', 'you', 'not', 'can', 'the', 'in', 'be', 'of', 'a']

Words dropped from Dictionary: ['properly' 'but' 'and']

Unconcatenated text: you  figure  that  you  can  add  back  in  the  punctation  a ND capitalisation  later  once  you  get  the  individual  words  proper LY separated  most  of  the  words  will  be  in  a  dictionary BUT some  strings  like  proper  names  will  not

Unrecognized characters:  7
</details>

## Remarks

- This tool doesn't always output the optimal solution, but it comes close to what a human would expect.
- There are some known errors this tool produces. For example, when there are single vowels (i.e: `a`, `I`) or small words  (i.e.: `an` `in`) on the input dictionary, and they are also present in the unknown words (i.e.: `minimizes`, `capitalization`), the tool wrongly unconcatenates the words, based on its incomplete dictionary (i.e.: `M in IMIZES`, `C a PIT a LIZ a TION`).


## Problem Description

Oh, no!

You have just completed a lengthy document when you have an unfortunate Find/Replace mishap. You have accidentally removed all spaces, punctuation, and capitalisation in the document.

A sentence like "I reset the computer. It still didn't boot!" would become iresetthecomputeritstilldidntboot".

You figure that you can add back in the punctation and capitalisation later, once you get the individual words properly separated. Most of the words will be in a dictionary, but some strings, like proper names, will not.


Given a dictionary (a list of words), design an algorithm to find the optimal way of "unconcatenating" a sequence of words. In this case, "optimal" is defined to be the parsing which minimizes the number of unrecognized sequences of characters.


For example, the string "jesslookedjustliketimherbrother" would be optimally parsed as "JESS looked just like TIM her brother". This parsing has seven unrecognized characters, which we have capitalised for clarity.

