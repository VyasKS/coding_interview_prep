from typing import List

""" Dynamic programming involves two approaches. Top-down & bottom-up. Top-down is via recursion & memoize (to avoid excess computations). Bottom-up with tabular iterations."""
"""
Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?"""


def climbing_stairs(n: int) -> int:
    # bottom up approach O(n) space complexity
    # if n == 1 or n == 2:
    #     return n
    # result = [0 for i in range(n)]
    # result[0], result[1] = 1, 2
    # for i in range(2, n):
    #     result[i] = result[i-1] + result[i-2]
    # return result[-1]
    # bottom up in constant space
    # if n == 1 or n == 2:
    #     return n
    # a, b = 1, 2
    # for i in range(2, n):
    #     temp = b
    #     b = a + b
    #     a = temp
    # return b
    # Top-down approach + memoization
    # find sub problem for n-1 & n-2 & add them up
    # No.of ways to reach step n = # of ways to reach n-1 + # of ways to reach n-2
    if n <= 2:
        return n
    s = {1: 1, 2: 2}
    if n not in s:
        s[n] = climbing_stairs(n - 1) + climbing_stairs(n - 2)
    return s[n]


""" House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that
adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police."""


def rob(nums: List[int]) -> int:
    # Fails for circular case [2,1,1,2]. Works only for adjacent cases. Check DP solution below.
    # approach in 2 ways. start with 0 & start with 1, in steps of 2
    # total, total2 = 0, 0
    # for i in range(0, len(nums), 2):
    #     total += nums[i]
    # for i in range(1, len(nums), 2):
    #     total2 += nums[i]
    # return max(total, total2)
    # -- Cool solution, but looks confusing ---
    # use recursive formula
    # f(0) = nums[0]
    # f(1) = max(num[0], num[1])
    # f(k) = max(f(k - 2) + nums[k], f(k - 1))
    # last, now = 0, 0
    # for i in nums:
    #     last, now = now, max(last + i, now)
    # return now
    # More clear solution is as follows:
    # Base Case: nums[0] = nums[0]
    # nums[1] = max(nums[0], nums[1])
    # nums[k] = max(k + nums[k-2], nums[k-1])
    # Approach 1:- Construct dp table
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    dp = [0] * len(nums)                # create a data structure to memoize
    dp[0] = nums[0]                     # feed in 1st & 2nd elements
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):       # iterate over all elements, capturing maximum of current + 2 steps before with 1 step before (compares 2 ways basically)
        dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
    return dp[-1]                       # return the last element


print(rob([2, 7, 9, 3, 1]))
