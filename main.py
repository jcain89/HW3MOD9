import functools
from collections import defaultdict, Counter

url = "http://raw.githubusercontent.com/eneko/data-repository/master/data/words.txt"
import os
from urllib.request import urlopen
wordfile = urlopen(url)
words = wordfile.read().decode('utf-8').upper().split()

def anagram(words):
    anagrams = defaultdict(list)
    for word in words:
        histogram = tuple(Counter(word).items()) # build a hashable histogram
        anagrams[histogram].append(word)
    return sorted(list(anagrams.values()))

def anagramChecker(word1: str, word2: str):
    if sorted(word1.upper()) == sorted(word2.upper()):
        return True
    return False

def isWordChecker(word):
    if words.__contains__(word.upper()):
        return True
    return False


def convert(s):
    # Using reduce to jion the list s to string
    str1 = functools.reduce(lambda x, y: x + y, s)

    # Return string 1
    return str1

def permutations(string, a, step = 0):
    if step == len(string):
        print("".join(string))
        print(string)
        a.append(convert(string))
        print(a)
        print(len(a))
        print(string[0])
        print("BREAK")
    for i in range(step, len(string)):
        # copy the string (store as array)
        string_copy = [c for c in string]
        print("STRING COPY :", string_copy)
         # swap the current index with the step
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
        print("SWAPPED STR COPY: ", string_copy)
         # recurse on the portion of the stringthat has not been swapped yet
        print("RECURSE TIME")
        permutations(string_copy, a, step + 1)
    return a


def permToList(string):
    results = []
    a = permutations(string, [], 0)
    for i in a:
        if isWordChecker(i):
            results.append(i)
        else:
            continue
    return results





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(type(permutations("earth", [])))
    a = str(permutations("earth", []))
    print("a is: ")
    print(a)
    print("first")
    print(a[0])
    print("---")
    print(permToList("EARTH"))
    print(isWordChecker("HERAT"))

