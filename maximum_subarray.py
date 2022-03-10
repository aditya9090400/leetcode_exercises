"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
"""
from typing import List


# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         largest = -10e4
#         for ind,ele in enumerate(nums):
#             sub_array_sum = 0
#             for sub_ele in nums[ind:]:
#                 sub_array_sum += sub_ele
#                 if sub_array_sum > largest:
#                     largest = sub_array_sum
#         return largest


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0

        for n in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += n
            max_sum = max(max_sum, curr_sum)
        return max_sum