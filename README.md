# i2x Vanhackaton challenge of 2017.

`unconcatenate_words.py` is a tool to unconcatenate strings (as "iwanttogotoberlin" -> "i want to go to berlin") using a given dictionary.

## Installation

```
$ git clone https://github.com/pedropb/i2x-challenge
$ pip install -r requirements.txt
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
<summary><pre>$ ./unconcatenate_words.py examples/text1</pre></summary>
Found and verified text8.zip
Concatenated text: YouhavejustcompletedalengthydocumentwhenyouhaveanunfortunateFindReplacemishapYouhaveaccidentallyremovedallspacespunctuationandcapitalisationinthedocument

Unconcatenated text: you  have  just  completed  a  lengthy  document  when  you  have  an  unfortunate  find  replace  mishap  you  have  accidentally  removed  all  spaces  punctuation  and  capitalisation  in  the  document

Unrecognized characters:  0
</details>

<details>
<summary><pre>$ ./unconcatenate_words.py examples/text2</pre></summary>
Found and verified text8.zip
Concatenated text: YoufigurethatyoucanaddbackinthepunctationandcapitalisationlateronceyougettheindividualwordsproperlyseparatedMostofthewordswillbeinadictionarybutsomestringslikepropernameswillnot

Unconcatenated text: you  figure  that  you  cana  dd  back  int  hep  unc T ation  and  capitalisation  later  once  you  get  the  individual  words  properly  separated  most  oft  he  words  will  bein  a  dictionary  but  some  strings  like  proper  names  wil  lnot
Unrecognized characters:  1
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

