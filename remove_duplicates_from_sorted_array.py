"""Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.
Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[x] = nums[i+1]
                x += 1
        return x, nums

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         nums = list(set(nums))
#         return len(list(set(nums))), nums