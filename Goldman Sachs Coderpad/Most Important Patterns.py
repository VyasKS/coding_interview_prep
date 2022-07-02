"""Following file contains most important patterns required for acing a coding interview. Questions were particularly filtered for Goldman Sachs.

1. Sliding Window
2. Two Pointers
3. Fast & Slow Pointers
4. Merge Intervals
5. Cyclic Sort
6. Tree - Breadth First Search
7. Tree - Depth First Search
8. Top K Elements
9. Topological Sort (Graphs)
10. Knapsack - Dynamic Programming

Look for other problems in Dynamic Programming - very important for Goldman Sachs.

SlIDING WINDOW : Delete element leaving out and Add element entering

Following is an example code for computing averages of contiguous arrays of size 5
"""


def find_averages_of_contiguous_sub_arrays(k, array):
    result = []  # store averages
    window_start, window_sum = 0, 0.0
    for window_end in range(len(array)):
        window_sum += array[window_end]  # add element to compute sum
        # keep adding until we reach window size, then move on to compute average and delete, add elements
        if window_end >= k - 1:
            result.append(window_sum / k)  # compute average & add to result array
            window_sum -= array[window_start]  # delete element leaving the window
            window_start += 1  # slide window by 1 position
    return f"Averages of contiguous sub arrays of size {k} is {result}"


# driver code
print(find_averages_of_contiguous_sub_arrays(k=5, array=[1, 2, 3, 4, 5, 6, 109, 111, 2314]))
""" Maximum Sum Subarray of Size K """


def max_sub_array(k, array):
    # Brute force approach. Start with every index, add next k elements & compute the sum
    """ BRUTE FORCE
    The time complexity of the above algorithm will be O(N∗K), where ‘N’ is the total number of elements in array.
    """
    # max_sum = 0
    # window_sum = 0
    # for i in range(len(array) - k + 1):     # until possible end of array for window size k
    #     window_sum = 0
    #     for j in range(i, i+k):
    #         window_sum += array[j]
    #     max_sum = max(window_sum, max_sum)
    # return max_sum
    """SLIDING WINDOW approach"""
    max_sum, window_sum = 0, 0
    window_start = 0
    for window_end in range(len(array)):    # add each element
        window_sum += array[window_end]
        # keep adding elements, no need to slide window until we hit window_size
        if window_end >= k - 1 :


# driver code
print(max_sub_array(k=3, array=[1, 2, 3, 4, 5, 6, 109, 111, 2314]))
