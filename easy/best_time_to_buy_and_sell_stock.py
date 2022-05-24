"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices = prices[::-1]
        max_profit = 0
        high_buy = 0

        for price in prices:
            if price > high_buy:
                high_buy = price
            if high_buy - price > max_profit:
                max_profit = high_buy - price
        return max_profit

obj = Solution()
prices = [7,1,5,3,6,4]
print(obj.maxProfit(prices))
