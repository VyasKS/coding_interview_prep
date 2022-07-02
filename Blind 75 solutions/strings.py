"""
Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once. https://leetcode.com/problems/valid-anagram/"""


def valid_anagram(s: str, t: str) -> bool:
    # Personal Solution
    count_s, count_t = {}, {}
    for c in s:
        if c not in count_s:
            count_s[c] = 1
        else:
            count_s[c] += 1
    for c in t:
        if c not in count_t:
            count_t[c] = 1
        else:
            count_t[c] += 1
    # Check anagram condition by matching counts
    return count_s == count_t
    # Easier way is to use sorted method
    # return sorted(s) == sorted(t)


"""
Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.https://leetcode.com/problems/valid-parentheses/"""


# Logic:
# Push opening brace on to stack. Pop if matching close brace is found (makes sures that order thus far is good)
# If stack is empty, return True, else False.


def valid_parentheses(s: str) -> bool:
    stack = []
    d = {"}": "{", "]": "[", ")": "("}
    for char in s:
        if char in d.values():
            stack.append(char)  # opening brace, append to stack
        elif char in d.keys():  # if a closing brace is found
            if stack == [] or d[char] != stack.pop():  # if a stack is already empty or closing brace is the not latest popped element of the stack
                return False  # return False
        else:
            return False  # return False in all other cases
    return stack == []  # stack should be empty


"""
Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers. Given a string s, return true if it is a palindrome, or false otherwise."""


def valid_palindrome(s: str) -> bool:
    # Personal solution, won't work for alphanum()
    # o = []
    # for char in s:
    #     if char.isdigit():          # Handle numeric characters
    #         return False
    #     if char.isalpha():          # Take only alphabets
    #         o.append(char.lower())
    #     else:                       # skip non-alphanumeric characters
    #         continue
    # r = list(reversed(o))           # reverse it, make a list out of reversed object
    # return o == r                   # check its truth
    # Optimized & easy solution
    left, right = 0, len(s) - 1
    while left < right:                                         # Two pointers left < right condition
        while left < right and not s[left].isalnum():           # is character is non alphanumeric, skip
            left += 1                                           # is character is non alphanumeric, skip
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():                 # left character should be same as right character in a palindrome
            return False
        left += 1
        right -= 1
    return True                                                 # true in all other cases


""" REVERSE A STRING WITHOUT USING SPLIT() METHOD IN PYTHON - ASKED IN A CODING INTERVIEW"""


def reverse_a_string(big_string):
    # Clean spaces with comma for separation
    cleaned = []
    for char in big_string:
        if char == " ":
            # print('Space found and splitting here')
            # remove space and concatenate
            i = big_string.index(char)       # get index position
            cleaned.append(big_string[:i])  # append word until space in a new list
            big_string = big_string[i+1:]   # update big_string
            if " " in big_string:           # if still a space in the whole string exists
                continue
            else:                           # last word reached, add it to cleaned
                cleaned.append(big_string)
    reversed_string_array = cleaned[::-1]
    final = ""
    for word in reversed_string_array:
        final = final+word+" "
    return final

