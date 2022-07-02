""" Following questions are from leetcode discussion forum
1. Find second smaller element in an array
"""
from typing import List
from collections import defaultdict


def second_best(test_array):
    def merge_sort(array):
        # Merge Sort the array in ascending order and retrieve the index[-2]
        if len(array) > 1:
            r = len(array) // 2  # r is mid-point of array
            left = array[:r]  # divide left half
            right = array[r:]  # and right half
            # Merge sort again recursively - divide & conquer into small pieces
            merge_sort(left)
            merge_sort(right)
            # Initialize pointers to compare items in two lists & add lowest first
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    array[k] = left[i]
                    i += 1
                else:
                    array[k] = right[j]
                    j += 1
                k += 1
            # Add left-over elements
            while i < len(left):
                array[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                array[k] = right[j]
                j += 1
                k += 1

            return array

    return merge_sort(test_array)
    # return sorted_input[5]  # 2nd element from last is 2nd highest


# Driver code
test = [1, 2, 4, 43, 32, 9, 34, 14, 442, 9234, 12, 102, 108]
print(second_best(test_array=test))

""" High-five: Given a list of the scores of different students, items, where items[i] = [IDi, scorei] represents one score from a student with IDi, calculate each student's top five average.

Return the answer as an array of pairs result, where result[j] = [IDj, topFiveAveragej] represents the student with IDj and their top five average. Sort result by IDj in increasing order.

A student's top five average is calculated by taking the sum of their top five scores and dividing it by 5 using integer division."""


# Solution approach 1: Sort the items based on IDs first & if there are two same score for an ID, then sort in descending order of scores among them
def high_five(array: List[List[int]]) -> List[List[int]]:
    result = defaultdict(list)
    # Add scores in a list for a student id
    for student, score in array:
        result[student].append(score)
    # sort in descending order of scores for each student id
    for scores in result.values():
        scores.sort(reverse=True)
        scores[5:] = []  # make an empty list beyond 5 scores
    return [[student, sum(scores) // 5] for student, scores in sorted(result.items())]


# Driver code
items = [[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]
print(high_five(items))


