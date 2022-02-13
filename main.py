from typing import List


def find_median(arr):
    new = sorted(arr)
    for index in range(len(new)):
        if index == (len(new) + 1) / 2:
            return new[index]


def remove_duplicates(num, val):
    start, end = 0, len(num) - 1
    # As long as our starting position is less than or equal to ending position
    while start <= end:
        # If value at starting position is same as val asked
        if num[start] == val:
            # Swap start with end value & move end position further left by 1 position
            num[start], num[end], end = num[end], num[start], end - 1
        else:   # Else, if value is different, move on to next index
            start += 1
        return start    # Finally, start position would've reached end of the array or elements. This is final length.


def unique_element(arr):
    for v in arr:
        if arr.count(v) == 1:
            return v

# def remove_duplicates(nums, val):
#     start, end = 0, len(nums) - 1
#     while start <= end:
#         if nums[start] == val:
#             nums[start], nums[end], end = nums[end], nums[start], end - 1
#         else:
#             start += 1
#     return start


def search_insert(nums: List[int], target: int) -> int:
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        elif target > nums[-1]:
            return len(nums)
        elif (nums[i] < target) and (target < nums[i + 1]):
            return i + 1

"""
# Kadane's algorithm in pseudo code to find maximum sum of a contiguous array (an array within array)
Whole idea here is to look for all positive contiguous segments of array(max_ending_here is used for this). And keep track of maximum sum contigous
segment among all positive segments. Briefly, we need to track two things. One pointer that tracks the overall largest sum we had seen so far &
another pointer that tracks where maximum value ends for a position. max_so_far will be an all-time high & max_ending_here gives current pos.

#### Psuedo code ####
Initialize:
    max_so_far = int_min
    max_ending_here = 0

Loop for each element of the array:
    max_ending_here = max_ending_here + a[i]
    if(max_so_far < max_ending_here):
        max_so_far = max_ending_here
    if(max_ending_here > 0):
        max_ending_here = 0
return max_so_far
"""


def kadane_algorithm_to_find_maximum_sum_in_contiguous_array_within_array(array: List[int], size: int) -> int:
    """ Kadane algorithm is an efficient way to output maximum sum of contiguous array within an array"""
    # Take care of corner case where only 1 -ve element in an array is given
    # Initialize variables of maximum sum and remember current position of the element of interest
    # Maximum tracks all time high for sum in the contiguous array within an array
    # Current position tracks current maximum value. If it is tracking a negative value, this will be overridden and set back to zero
    max_sum_so_far = array[0]
    current_max_sum = 0
    # Iterate through all elements in the array
    for i in range(0, size):
        # Update current_max_sum with the element of iteration
        current_max_sum = current_max_sum + array[i]
        # Check if current_max_sum is a negative value, if so, set it back to zero
        if current_max_sum < 0:
            current_max_sum = 0
        # Check if max_sum_so_far keeps up with current_max_sum to update all time high
        if max_sum_so_far < current_max_sum:
            max_sum_so_far = current_max_sum
    # Get the final max_sum_so_far and return it on console
    print(f"Maximum sum for the contiguous array within an array is found to be {max_sum_so_far}")
    return max_sum_so_far


# Finds max sum of contiguous array (array within array)
def kadane_algorithm(nums: List[int], size: int) -> int:
    # Initialize two pointers. One for remembering current position & the other for keeping the count
    max_so_far = nums[0]    # This avoids a corner case when there's only 1 element in the array (e.g. [-1], then max.sum = -1)
    max_ending_here = 0
    # Iterate through each element in the array
    for i in range(0, size):
        max_ending_here += nums[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here    # Update max_so_far if max_ending_here went beyond max_so_far value
        if max_ending_here < 0:
            max_ending_here = 0             # If position keeper is -ve, set it back to zero. There's no point in tracking negative sums.
    return max_so_far


# Rewriting kadane's algorithm to find maximum sum of contiguous array (array within array)
def max_sum_contiguous_array(array: List[int], size: int) -> int:
    # Initialize variables
    maximum_sum_till_now = a[-1]
    current_max_position = 0
    # Iterate through each element in the array
    for i in range(0, size):
        current_max_position += array[i]
        # Update maximum sum
        if maximum_sum_till_now < current_max_position:
            maximum_sum_till_now = current_max_position
        # If current element is negative, ignore it and set it back to zero
        if current_max_position < 0:
            current_max_position = 0
    return maximum_sum_till_now


def kadane_algorithm_practice(array: List[int], size: int) -> int:
    # Initialize variables
    max_sum_till_now = a[0]     # Takes care of corner case where first element is a negative
    current_position = 0
    # Iterate through each element in the array
    for i in range(0, size):
        current_position += a[i]
        # If current position is a -ve number, set it back to zero
        if current_position < 0:
            current_position = 0
        # If maximum sum so far is less than current_position, update it and set as all time high
        if max_sum_till_now < current_position:
            max_sum_till_now = current_position
    # End of the iteration should produce the overall sum for the contiguous array
    print(f"Maximum sum for the contiguous array would be ...")
    return max_sum_till_now


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list1 = [3, 5, 7, 23, 33, 3, -1, 4, -1, 99, 7, 4, 5, 1073, 345]
    # mylist = ["a", "b", "a", "d", "c", "c", "a", "c"]
    # print(remove_dups(mylist, 'c'))
    #r = remove_duplicates(mylist, 'c')
    #print(r)
    #a = find_median(list1)
    #print(a)
    #print(search_insert([1, 3, 5, 6], 7))
    # Check the kadane algorithm with the below array
    a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
    d = [-1]
    #print(f"Maximum contiguous sum is {kadane_algorithm(d, len(d))}")
    #print(f"Maximum sum of the contiguous array is {max_sum_contiguous_array(list1, len(list1))}")
    #print(max_sum_contiguous_array(array=a, size=len(a)))
    print(kadane_algorithm_to_find_maximum_sum_in_contiguous_array_within_array(array=list1, size=len(list1)))
