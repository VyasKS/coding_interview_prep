# Level 1 : Peak Element
# An element is called a peak element if its value is not smaller than the value of its adjacent elements(if they exist).
# Given an array arr[] of size N, find the index of any one of its peak elements.

def peak_element(arr, n):
    # if n == 1:
    #     return 0
    # if n == 2:
    #     for i in range(n):
    #         return i if arr[i] > arr[i + 1] else i + 1
    # # for len > 2
    # max_so_far, current = 0, arr[0]
    # for i in range(n):
    #     if arr[i] > max_so_far:
    #         max_so_far = arr[i]
    #     if max_so_far < current:
    #         max_so_far = current
    # return arr.index(max_so_far)
    # Using inbuilt max function
    return 0 if n == 1 else arr.index(max(arr))


# Level 1: Find maximum and minimum element in an array : Given an array A of size N of integers. Your task is to find the minimum and maximum elements in the array.
def get_min_max(arr, n):
    # using libraries
    # minimum = min(arr)
    # maximum = max(arr)
    # return minimum, maximum
    # Without libraries
    current, minimum, maximum = 0, float("inf"), float("-inf")
    for i in range(n-1):
        if arr[i] > maximum:
            maximum = arr[i]
        if arr[i] < minimum:
            minimum = arr[i]
        current = arr[i]
        if maximum < current:
            maximum = current
        if minimum > current:
            minimum = current
    return minimum, maximum


# Level 2: Find missing integer in an array. Sorting first and then calling in another funtion "get_missing()"
def merge_sort(array):
    if len(array) > 1:
        # split array at mid-point
        mid = len(array) // 2
        l = array[:mid]
        r = array[mid:]
        # call recursive merge_sort
        merge_sort(l)  # sort first half
        merge_sort(r)  # sort second half
        # initialize pointers
        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                array[k] = l[i]  # k is index of final array element
                i += 1  # move i pointer by 1
            else:
                array[k] = r[j]  # add jth element to final array
                j += 1  # move j pointer by 1
            k += 1  # move pointer by 1 point
        # Handle left over elements
        while i < len(l):
            array[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            array[k] = r[j]
            j += 1
            k += 1
    return array


def get_missing(array):
    # Fails if missing value is in the last place
    sorted_array = merge_sort(array)
    for i in range(len(sorted_array)):
        if sorted_array[i + 1] - sorted_array[i] > 1:
            return sorted_array[i] + 1


# Sum of elements 1 to n is given by formula [N * (N+1) / 2]
def get_missing_using_summation(array):
    # if the length of correct array is already given, start from there. else, add 1 to length of existing array with missing value
    n = len(array)
    total = (n+1) * (n+2) / 2     # starting with n+1 because, 1 element is already missing, so original length should be n+1.
    sum_array = sum(array)
    return total - sum_array





















