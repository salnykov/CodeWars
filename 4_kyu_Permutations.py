    # In this kata, your task is to create all permutations of a non-empty input string and remove duplicates, if present.
    #
    # Create as many "shufflings" as you can!
    #
    # Examples:
    #
    # With input 'a':
    # Your function should return: ['a']
    #
    # With input 'ab':
    # Your function should return ['ab', 'ba']
    #
    # With input 'abc':
    # Your function should return ['abc','acb','bac','bca','cab','cba']
    #
    # With input 'aabb':
    # Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
import itertools
import time
import random


def permutations(s):
    perms = set(itertools.permutations(s))
    result = ["".join(item) for item in perms]
    return result

def permutations2(string):
    return list("".join(p) for p in set(itertools.permutations(string)))

start = time.time()
string = "abcdefghijk"

permutations(string)
print(f"Time taken by my algorithm: {time.time()-start} seconds")

start = time.time()

permutations2(string)
print(f"Time taken by proposed algorithm: {time.time()-start} seconds")


