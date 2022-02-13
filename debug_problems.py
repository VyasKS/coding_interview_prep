from typing import List


# Arrays practice
def find_max_consecutive_ones(nums: List[int]) -> int:
    # initialize count
    count = 0
    # initialize max
    result = 0
    for i in range(0, len(nums)):
        # Reset count when 0 is found
        if nums[i] == 0:
            count = 0
        # If 1 is found, increment count
        # and update result if count
        # becomes more.
        else:
            # increase count
            count += 1
            result = max(result, count)

    return result


def find_even_digit_nums(nums: List[int]) -> int:
    """ return # of integers with only an even number of digits """
    count = 0
    for i in nums:
        z = len(str(i))
        if z % 2 == 0:     # if l is even
            count += 1
    return count


def squares_of_sorted_array(nums: List) -> int:
    """ Get squares of each element sorted as non-decreasing"""
    # Create a new array, add squared elements into it, then figure out sorting
    new = []
    for e in nums:
        new.append(e*e)
    # sort
    new.sort()
    return new


# DUPLICATE ZEROES IN ARRAY BY SHIFTING ELEMENTS TO RIGHT, ARRAY WILL BE OF FIXED SIZE, NOT DYNAMIC, THEREFORE LOSS OF SOME ELEMENTS COULD BE IMMINENT
def duplicate_zeros(arr: List[int]) -> None:
    i = 0
    while i < len(arr) - 1:         # loop from start to end of array
        if arr[i] == 0:             # if we found 0
            arr.insert(i+1, 0)      # insert a 0 at index i+1
            del arr[len(arr)-1]     # delete last element now
            i = i + 2               # set index to i+2. We don't want i+1, as we inserted 0 there & don't want to cause a recurrent zero insertion because of our insertion
        else:
            i = i + 1               # set index to next element
    # This completes in-place operation of zero insertion


# Merge two lists and sort them, replace extra zeros in first list with elements of second list & then sort it. Here, list 2 is inserted into list 1. Lists & sizes are given
def merge_two_lists(nums1: List[int], m, nums2: List[int], n) -> None:
    """
    :param nums1: Integer array
    :param m : size of nums1 elements only, not whole array size with 0s
    :param nums2: Integer array
    :param n : size of nums2
    :returns None. Performs in-place operation on nums1"""
    # 2 Pointer approach is best with O(k) time and O(1) memory complexities respectively
    p1 = m-1    # End of nums1 array elements, not zeros
    p2 = n-1    # End of nums2 array elements
    i = m+n-1   # End of nums1 elements + 0s..Last element in nums1 including zeros
    while p2 >= 0:  # As long as there's an element in nums2, takes care of edge case where nums1[0] has no integer other than empty space & nums2[-1] has a -1, which is less than to compare
        if p1 >= 0 and nums1[p1] > nums2[p2]:   # Check if element at p1 is > element at p2. We compare and insert according to the order
            nums1[i] = nums1[p1]        # Replace zero with element at p1
            i -= 1
            p1 -= 1
        else:
            nums1[i] = nums2[p2]        # Replace with element at p2, decrement pointer locations
            i -= 1
            p2 -= 1


# Delete items from an array. For every occurrence of val in nums, delete it in-place. Relative order of elements may be changed and freed up space could be anything. In Python, we can simply delete
# & return final k number of elements left behind in the array
def remove_element(arr, val):
    counter = 0
    for i in range(len(arr)):
        if arr[counter] == val:
            arr.pop(counter)
        else:
            counter += 1
    print(arr)


def removeDuplicates(nums: List[int]) -> int:
    if len(nums) == 1:
        return 1
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1

    # """Solution 2 using pointers"""
    # # Remove val in arr
    # start, end = 0, len(arr)-1
    # for i, v in enumerate(arr):
    #     if v == val:
    #         arr[start] = arr[end]
    #         arr[end] = arr[start]
    #         end -= 1
    # print(start)
    #
    # array = arr
    # for i, v in enumerate(array):
    #     if v == val:
    #         array.pop(i)
    #         array = array


if __name__ == '__main__':
    test = [1,1,1,1,1,3]
    #print(find_max_consecutive_ones(test))
    #a = [555, 901, 482, 1771]
    #print(find_even_digit_nums(a))
    #b = [-4, -1, 0, 3, 10]
    #print(squares_of_sorted_array(b))
    #a = [1,2,3,0,0,0]
    #b = [4,5,6]
    #print(merge_two_lists(a, len(a), b, len(b)))
    #print(remove_element(arr=test, val=1))
    print(removeDuplicates(test))
