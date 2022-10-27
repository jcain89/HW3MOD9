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

def createSet(s):
    sol = []
    wordSet = list(s)
    alph: str = "ABCDEFFGHIJKLMNOPQRSTUVWXYZ"
    for l in alph:
        wordSet.append(str(l))
        wordSet.sort()
        for a in words:
            x = (list(a))
            x.sort()
            if x == wordSet:
                sol.append(a)
        wordSet = list(s)
    print(sol)
    print(type(wordSet))

#I changed my time complexity from O(n!) to O(n)









# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(createSet("HERAT"))

