import collections
""" This file contains practice of problems asked in the Cracking the Coding Interview Book """


# Implement an algorithm to determine if a string has all unique characters, without the use of additional data structures
def is_unique(string:str) -> bool:
    # Not so efficient but an easy way is to use set(). It only keeps unique elements in an iterable (list, dict & tuple)
    if len(string) > len(set(string)):      # If original length is more than set(string)'s length? means repeated characters
        return False
    return True
    # Same code applies for arrays, dictionaries & tuples too. Applying set on dictionary will keep only keys & values are get
    # lost


# Check Permutation. Given two strings, write a method to decide if one is a permutation of the other.
def check_permutation(string1: str, string2: str) -> bool:
    # Check all characters of string1 exist in string2. If so, its a permutation. Else, no.
    # Count of a string is list of :[# of a's, # of b's,...# of z's]
    # Using counter.collections(), we get count for each element in the list/string as a dict object
    counter1 = collections.Counter(string1)
    counter2 = collections.Counter(string2[:len(string1)])  # Counter object length should be same as length of string1
    # Keep two pointers i(front), j(last), delete & add accordingly, check for the counts
    i, j = 0, len(string1)
    # Run a while loop to check if we are able to match the counter2 in counter1 by sliding over all elements in string2
    while j < len(string2):
        if counter2 == counter1:
            return True                 # We found a permutation if both counts are same
        counter2[string2[i]] -= 1       # We delete count of ith element in string2, to slide it forward
        if counter2[string2[i]] < 1:    # if the count of ith element is 0, pop from counter
            counter2.pop(string2[i])
        counter2[string2[j]] = counter2.get(string2[j], 0) + 1
        i += 1
        j += 1
    return counter2 == counter1
