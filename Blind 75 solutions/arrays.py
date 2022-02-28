from typing import List

"""Two Sum: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, 
and you may not use the same element twice. You can return the answer in any order. https://leetcode.com/problems/two-sum/ """


def two_sum(arr: List[int], target: int) -> List[int]:
    # Your solution in O(n2)
    # for i in range(len(arr)):
    #     for j in range(i+1, len(arr)):
    #         if arr[i] + arr[j] == target:
    #             return [i, j]
    # Best solution is to iterate through just once. Here, logic is x + y = target, and find indices of x & y in list
    # change eq. slightly to pass just once instead of loop inside a loop. x = target - y. Track visited elements in a dict.
    d = {}  # create empty dict to track visited elements. Key is element, value is index in list
    for i, v in enumerate(arr):  # loop just once
        m = target - v  # compute diff. to target
        if m in d:  # if that diff. in already visited elements
            return [d[m], i]  # return indices of both elements
        d[v] = i  # else add visited element in the dict


""" Best Time to Buy and Sell Stock: You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0. https://leetcode.com/problems/best-time-to-buy-and-sell-stock/"""

""" -------------------K A D A N E----A L G O R I T H M-------------------
    # Initialize:
        max_so_far = INT_MIN
        max_ending_here = 0
    # Loop for each element of the array
        1. max_ending_here = max_ending_here + a[index]
        2. if(max_so_far < max_ending_here)
                max_so_far = max_ending_here
        3. if(max_ending_here < 0)
                max_ending_here = 0
    return max_so_far
"""


def max_profit(prices: List[int]) -> int:
    # Your base solution. Runs in O(n2) and gives TLE - Time limit exceeded error
    # profit = 0
    # for i in range(len(prices)):
    #     for j in range(i+1, len(prices)):
    #         diff = prices[j] - prices[i]
    #         if diff > profit:
    #             profit = diff
    # return profit
    # Best implementation is to use kadane's algorithm
    maximum_profit, minimum_price = 0, float('inf')
    for price in prices:
        minimum_price = min(minimum_price, price)
        profit = price - minimum_price
        maximum_profit = max(maximum_profit, profit)
    return maximum_profit


""" Duplicate: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
https://leetcode.com/problems/contains-duplicate/"""


# We can implement same methodology as two_sum and pass through the list just once. Create a dict & track visited elements. If element already in dict, true.
# O(n) linear growth


def duplicate(nums: List[int]) -> bool:
    # Your solution
    t = []  # create a data structure to track
    for i in nums:  # for element in nums, not index in range()
        if i in t:  # if element in tracked list
            return True
        t.append(i)  # else append it to tracked list
    return False  # loop ends & no duplicate found, return False
    # One line better solution is to use set(). This will discard duplicates
    # return len(nums) != len(set(nums))


""" Product of Array Except Self:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer. You must write an algorithm that runs in O(n) time and without using the division operation.
https://leetcode.com/problems/product-of-array-except-self/
"""


def product_except_self(nums: List[int]) -> List[int]:
    # Own solution. But fails with largest inputs. Below is an optimal solution therefore.
    # Take one index, multiply rest of the elements and store value at the index position in a new array
    # Use a stack to pop the index, multiply rest and store in answer array. Replace back the element at index. Repeat.
    # result = 1
    # answer = []
    # for i in range(len(nums)-1):
    #     popped = nums.pop(i)     # popped the element
    #     for x in nums:
    #         result *= x
    #     answer[i] = result      #
    #     nums.insert(i, popped)
    # return answer
    # Optimized solution from leetcode discussion. First part of the loop multiplies all elements before, second part after.
    # compute prefix (vals before element), postfix(vals after element) - output is just multiplying left & right element to it.
    # check explanation here : https://www.youtube.com/watch?v=bNvIQI2wAjk
    p = 1
    n = len(nums)
    output = []
    for i in range(0, n):  # Compute product of elements before n (prefix products from left to right)
        output.append(p)
        p = p * nums[i]
    p = 1
    for i in range(n - 1, -1, -1):  # Compute product of elements after n (prefix products from right to left a.k.a. postfix from left to right)
        output[i] = output[i] * p
        p = p * nums[i]
    return output


""" Maximum Sub array :
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array. (https://leetcode.com/problems/maximum-subarray/)
"""


# Negative and zero values have importance to this problem. Having zero makes entire array 0, so should exclude it. Even # of -ves is a positive. Have to
# consider this when coming up with a solution.
def max_sub_array(nums: List[int]) -> int:
    # Kadane algorithm - Two variables. One to track all time high sum & the other that remembers current sum @ respective element
    max_so_far = nums[0]  # Avoids corner case (e.g. [-1], here sum is -1)
    max_ending_here = 0
    # Iterate through each element in the array
    for i in range(0, len(nums)):
        # First update max_ending_here to remember position
        max_ending_here += nums[i]
        # Now, if max_so_far is < max_ending_here, update it
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        # Now, if max_ending_here is < 0, set it to zero. No point in tracking negative sums
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far  # Contiguous sum for an array


"""
Maximum Product Subarray: Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer. A subarray is a contiguous subsequence of the array. https://leetcode.com/problems/maximum-product-subarray/"""


def max_product_sub_array(nums: List[int]) -> int:
    # PERSONAL SOLUTION form Kadane algorithm - same as above. Replace sum with product increment
    # Fails for [0,2] or [2,0]
    # max_product_so_far = nums[0]   # Avoids corner cases ([-1])
    # max_ending_here = 1
    # for i in range(len(nums)):
    #     # Update current position
    #     max_ending_here *= nums[i]
    #     # If max_product_so_far falls behind, update it
    #     if max_product_so_far < max_ending_here:
    #         max_product_so_far = max_ending_here
    #     # Set to 0, if current position is -ve
    #     if max_ending_here < 0:
    #         max_end_here = 1
    # return max_product_so_far
    # Have two pointers max_prod & min_prod that track maximum & minimum values in an array. Read each element & if positive, all good.
    # If -ve, multiply it with these pointers, swap their values assuming min_product is already -ve. Solution inspired from https://www.youtube.com/watch?v=bpMDJ1rktmE
    max_prod, min_prod, result = nums[0], nums[0], nums[0]
    for i in range(1, len(nums)):  # Traverse through the array from 1, as initial element already assigned
        if nums[i] < 0:  # if a -ve value, swap max & min
            tmp = min_prod
            min_prod = max_prod
            max_prod = tmp
        # max_prod becomes new number(after zero) if encountered a zero. Same for min_prod. This takes care of zero values.
        max_prod = max(max_prod * nums[i], nums[i])
        min_prod = min(min_prod * nums[i], nums[i])
        result = max(result, max_prod)
    return result


""" Search in Rotated Sorted Array: There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity. https://leetcode.com/problems/search-in-rotated-sorted-array/
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1 """


def search_rotated_sorted_array(nums: List[int], target: int) -> int:
    # Got 2 personal solutions: 1st one is simple : O(n), second is writing a binary search algorithm : O(log n)
    if target not in nums:
        return -1
    else:
        for i, v in enumerate(nums):
            if target == v:
                return i
    # Binary search is an alternative, but only works on sorted arrays.


"""3Sum: Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets. https://leetcode.com/problems/3sum/
Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:
Input: nums = []
Output: []
Example 3:
Input: nums = [0]
Output: []
"""


def _3sum(nums: List[int], target):
    # Brute force method to iterate thrice in O(n**3). Gets only one combination. Fails to get multiple combinations.
    # for i in range(len(nums)-2):
    #     for j in range(i+1, len(nums)-1):
    #         for k in range(j+1, len(nums)):
    #             agg = nums[i]+nums[j]+nums[k]
    #             if agg == 0:
    #                 return [i, j, k]
    # return []
    """FAILS FOR NEGATIVE NUMBERS THOUGH.."""
    # Working solution: https://leetcode.com/problems/3sum/discuss/7498/Python-solution-with-detailed-explanation
    # # Better optimized solution: Sort the array to increase efficiency to O(n2)
    # Similar thinking as two_sum(). x + y + z = 0, change it as x + y = - z. Track difference in a dict (value : index). Traverse through array twice in O(n2)
    # Sort the array first in increasing order
    # Start with first element in array. Keep two pointer left & right. Increment the left pointer to one position if sum < 0; else if sum > 0: decrement right pointer by 1 position
    # return sum (which is triplet = array[i] + array[left] + array[right] if its equal to our target sum
    nums.sort()
    n, result = len(nums), []
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:  # We should avoid duplicates. Continues to next iteration
            continue
        target = nums[i] * -1  # Changing the sign
        s, e = i + 1, n - 1  # remaining array pointers start (left), right (end)
        while s < e:
            if nums[s] + nums[e] == target:  # If triplet found, append it to list
                result.append([nums[i], nums[s], nums[e]])
                s = s + 1  # move to next index
                while s < e and nums[s] == nums[s - 1]:  # avoids another duplicate after triplet
                    s = s + 1
            elif nums[s] + nums[e] < target:  # increment left by one if less than 0, else decrement right by one in remaining array
                s = s + 1
            else:
                e = e - 1
    return result


"""Container with most water:
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]). Find two lines that together with the
x-axis form a container, such that the container contains the most water. Return the maximum amount of water a container can store. Notice that you may not slant the container.
https://leetcode.com/problems/container-with-most-water/
"""


def container_with_most_water(height: List[int]) -> int:
    # Brute force solution: run two loops, for every element, compute area by checking the minimum value (limiting factor) otherwise water spills
    # max_area = float('-inf')
    # for i in range(len(height)):  # outer loop
    #     for j in range(i + 1, len(height)):  # inner loop
    #         limiting_factor = min(height[i], height[j])  # get minimum of both heights, coz of limiting factor (y-axis)
    #         max_area = max(max_area, limiting_factor * (j - i))  # multiply min height with distance btwn i & j (x-axis), update max_area if > previous
    # return max_area
    # Brute force solution produces TLE - time limit exceeded
    # Optimized solution:
    # use a while loop: start with extreme end & beginning pointers, compute area
    # decrement 1 step either sides, if next height is higher > previous both positions, move pointer
    # compute areas & store if > max_area
    start, end, max_area = 0, len(height) - 1, 0
    while start < end:
        if height[start] < height[end]:
            area = height[start] * (end - start)
            start += 1
        else:
            area = height[end] * (end - start)
            end -= 1
        max_area = max(max_area, area)
    return max_area
