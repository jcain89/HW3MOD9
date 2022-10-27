import functools
from collections import defaultdict, Counter

url = "http://raw.githubusercontent.com/eneko/data-repository/master/data/words.txt"
import os
from urllib.request import urlopen
wordfile = urlopen(url)
words = wordfile.read().decode('utf-8').upper().split()



def step(s):
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
#I changed my time complexity from O(n!) to O(n) below was the code that was O(n!)

"""def anagram(words):
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
    print(type(string))
    results = []
    a = permutations(string, [], 0)
    for i in a:
        if isWordChecker(i):
            results.append(i)
        else:
            continue
    return results

def step(input: str):
    allwords = []
    sol = permToList(input)
    import string
    alph: str = "ABCDEFFGHIJKLMNOPQRSTUVWXYZ"
    for l in alph:
        if l == []:
            pass
        print("First loop item")
        temp = ""
        print(type(l))
        print(type(input))
        temp = l + input
        print(temp)
        if permToList(temp) == []:
            pass
        else:
            allwords.append(permToList(temp))
            print("END OF LETTER: ", l)
    return allwords"""

if __name__ == '__main__':
    step("APPLE")
    step("UC")
    step("BEARCAT")





