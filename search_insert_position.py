"""
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        elif target < nums[0]:
            nums.insert(0, target)
            return 0
        elif target > nums[-1]:
            nums.insert(len(nums), target)
            return len(nums)-1
        else:
            for i in range(len(nums)-1):
                if target > nums[i] and target < nums[i+1]:
                    nums.insert(i+1, target)
                    return i+1
        
