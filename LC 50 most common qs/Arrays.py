from typing import List

"""
Arrays and Strings
1. Two Sum
2. Two Sum II - Input array is sorted
3. Two Sum III - Data Structure design
4. Valid Palindrome
5. Reverse words in a string
6. Reverse words in a string II
7. String to integer (AtoI)
8. Valid Number
9. Longest substring without repeating characters
10. Longest substring with at most two distinct characters
11. Missing ranges
12. Longest palindromic substring
13. One edit distance
14. Read n characters given Read4
15. Read n characters given Read4 - call multiple times
"""

"""Two Sum: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.
https://leetcode.com/problems/two-sum/
O(n2) runtime, O(1) space with Brute force
O(n) runtime, O(n) space with Hash table
"""


def two_sum(arr: List[int], target: int) -> List[int]:
    d = {}  # create empty dict to track visited elements. Key is element, value is index in list
    for i, v in enumerate(arr):  # loop just once
        m = target - v  # compute diff. to target
        if m in d:  # if that diff. in already visited elements
            return [d[m], i]  # return indices of both elements
        d[v] = i  # else add visited element in the dict


"""Two Sum - when input array is sorted in ascending order. O(n log n) runtime, O(1) space – Binary search"""


def binary_search(array, left, key):
    right = len(array) - 1
    mid = left + right // 2
    if key == array[mid]:
        return mid
    if key > array[mid]:
        left = mid
    else:
        right = mid
    return binary_search(array, left, key)


array = [1, 2, 3, 4, 5, 6, 109, 111, 2314]
# print(binary_search(array, left=0, key=2314))


def two_sum_II(numbers: List[int], target: int) -> List[int]:
    # Brute force approach: run 2 for loops, one for current position, the other for searching balance amount in the rest of the array
    """ Time complexity : O(n**2) for nested for loops"""
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)-2):
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
    return [-1, -1]   # if no such element

    # Use same approach as two_sum. But this fails if the tracked sum appears later in the array.
    # Alternative approach with constraint of using constant space, is given below.
    tracker = {}
    # for i, v in enumerate(numbers):
    #     if target-v in tracker:
    #         return [i+1, (tracker[target-v])+1]
    #     else:
    #         tracker[v] = i

    """ Using Binary Search  O(n log n) time , O(1) space.
    For each element x, we could look up target - x exists in O(log n) time using binary search over sorted array, so for n elements = O(n log n) """






    """ TWO POINTERS solution : O(n) runtime, O(1) space complexity """




print(two_sum_II(numbers=array, target=9))


def two_pass_ds_design():
    pass


"""Valid palindrome"""


def valid_palindrome(sample_string):
    left = 0
    right = len(sample_string)-1
    while left < right:
        if left < right and not sample_string[left].isalnum():
            left += 1
        if left < right and not sample_string[right].isalnum():
            right -= 1
        if sample_string[left].lower() != sample_string[right].lower():
            return False
        left += 1
        right -= 1
    return True


"""Reverse words in a string"""
def reverse_words(sample_string):
    words = []
    for i, character in enumerate(sample_string):
        if len(sample_string) > 1:
            if character == " ":
                words.append(sample_string[:i])
                sample_string = sample_string[i+1:]
    return words

#print(reverse_words("the sky is blue"))