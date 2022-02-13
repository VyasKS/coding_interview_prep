from typing import List
""" Leet code top 50 questions hand picked by the author of Blind 75, which is a superset of these 50 questions.
Checkout the preparation plan has been given at https://techinterviewhandbook.org/best-practice-questions/"""

""" ----------------------   WEEK 1 -------------------------
Two Sum: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, 
and you may not use the same element twice. You can return the answer in any order. """


def two_sum(arr: List[int], target: int) -> List[int]:
    # Your solution in O(n2)
    # for i in range(len(arr)):
    #     for j in range(i+1, len(arr)):
    #         if arr[i] + arr[j] == target:
    #             return [i, j]
    # Best solution is to iterate through just once. Here, logic is x + y = target, and find indices of x & y in list
    # change eq. slightly to pass just once instead of loop inside a loop. x = target - y. Track visited elements in a dict.
    d = {}                              # create empty dict to track visited elements. Key is element, value is index in list
    for i, v in enumerate(arr):         # loop just once
        m = target - v                  # compute diff. to target
        if m in d:                      # if that diff. in already visited elements
            return [d[m], i]            # return indices of both elements
        d[v] = i                        # else add visited element in the dict


""" Duplicate: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct."""
# We can implement same methodology as two_sum and pass through the list just once. Create a dict & track visited elements. If element already in dict, true.
# O(n) linear growth


def duplicate(nums: List[int]) -> bool:
    # Your solution
    t = []              # create a data structure to track
    for i in nums:      # for element in nums, not index in range()
        if i in t:      # if element in tracked list
            return True
        t.append(i)     # else append it to tracked list
    return False        # loop ends & no duplicate found, return False
    # One line better solution is to use set(). This will discard duplicates
    # return len(nums) != len(set(nums))


""" Best Time to Buy and Sell Stock: You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0."""

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
    # Your base solution. Runs in O(n2) and gives TLE - Time limit exceeded error on leetcode
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


""" Valid Anagram : Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once."""


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


""" Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    
    Input test cases are always in order. For e.g. () or [()] or {[()]}. If not order, can throw False.
"""
# Logic to check if this is a valid parentheses. First, write a while loop that executes as long as the condition satisfies matching
# As long as there exists a parentheses in right order (for all types), check for a matching close. Pop these two from the array and append
# it to the tuple. Do this for all elements in the string array. If the final string is not empty, then it is not a valid parentheses.


def valid_parentheses(s: str) -> bool:
    # Own solution. Won't work if order is not followed. Check correct solution implemented below.
    # We have totally 6 different cases: (,), [,],{,}
    # All brackets must be in order of open & close. Close comes only after open. For every open, there must be a close.
    # count_pairs = 0
    # for i in range(len(s)-1):
    #     if s[i] == '(' and s[i+1] == ')':
    #         count_pairs += 2
    #     elif s[i] == '[' and s[i+1] == ']':
    #         count_pairs += 2
    #     elif s[i] == '{' and s[i+1] == '}':
    #         count_pairs += 2
    # if len(s) == count_pairs:
    #     return True
    # return False
    # Solution that works. Elegant usage of stack & pop method to check close bracket
    stack = []                              # create an empty array - to push & pop elements traversing through order of characters
    d = {')': '(', ']': '[', '}': '{'}      # init a dict like this. Its imp, coz we've to check dict[char] later with popped value
    for char in s:                          # loop over entire string
        if char in d.values():              # if character matches with values in dictionary, means open type
            stack.append(char)              # append it to stack
        elif char in d.keys():              # if character matches with keys in dictionary, means closing type
            if stack == [] or d[char] != stack.pop():       # if stack empty or dict[char] is not same as last popped element
                return False                # return False. If true, last popped element must be in values of dict right? as input is always in order
        else:
            return False                    # In all other cases of input (e.g.unordered, empty etc.) return False
    return stack == []                      # stack must be empty after pushing & popping the element


""" Product of Array Except Self:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer. You must write an algorithm that runs in O(n) time and without using the division operation.
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
    for i in range(0, n):           # Compute product of elements before n (prefix products from left to right)
        output.append(p)
        p = p * nums[i]
    p = 1
    for i in range(n - 1, -1, -1):  # Compute product of elements after n (prefix products from right to left a.k.a. postfix from left to right)
        output[i] = output[i] * p
        p = p * nums[i]
    return output


# """ Maximum Subarray: return maximum sum of contiguous sub array in an integer array"""
def max_sub_array(nums : List[int]) -> int:
    # Use kadane algorithm




if __name__ == '__main__':
    test = [1, 1, 1, 1, 1, 3]
    a = [555, 901, 482, 1771, 2, 3, 1]
    b = [-4, -1, 0, 3, 10]
    # a = [1,2,3,0,0,0]
    # b = [4,5,6]
    #print(two_sum([3, 2, 4], target=6))
    #print(duplicate([3, 4, 5, 6, 7, 0]))
    # prices = [7, 1, 5, 3, 6, 4] # [7,6,4,3,1]
    # print(max_profit(prices))
    #print(valid_anagram(s="anagram", t="nagaram"))
    print(valid_parentheses(s="()[]{}"))

