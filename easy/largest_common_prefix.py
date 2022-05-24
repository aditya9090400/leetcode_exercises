"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings."""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        res = ""
        for st in strs[1:]:
            len1 = len(first)
            len2 = len(st)
            if len1 < len2:
                sm = len1
            else:
                sm = len2
            for i in range(sm):
                print(i)
                if first[i] == st[i]:
                    res += first[i]
                else:
                    break
            first = res
            res = ""
        return first
        
obj = Solution()
strs = ["flower","flow","flight"]
strs1 = ["dog","racecar","car"]
strs2 = ["dogiie","dogracecar","dogcar"]
st3 = ["cir","car"]
st4 = []
print(obj.longestCommonPrefix(strs))
print("===========================")
print(obj.longestCommonPrefix(strs1))
print("===========================")
print(obj.longestCommonPrefix(strs2))
print("===========================")
print(obj.longestCommonPrefix(st3))
print("===========================")
