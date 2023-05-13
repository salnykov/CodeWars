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


def permutations(s):
    perms = set(itertools.permutations(s))
    result = ["".join(item) for item in perms]
    return result

print(permutations("abba"))


