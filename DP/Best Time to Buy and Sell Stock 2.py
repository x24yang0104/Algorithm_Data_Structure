"""
Description
Given an array prices, which represents the price of a stock in each day.
You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, if you already have the stock, you must sell it before you buy again).

Example 1:
Input: [2, 1, 2, 0, 1]
Output: 2
Explanation: 
    1. Buy the stock on the second day at 1, and sell the stock on the third day at 2. Profit is 1.
    2. Buy the stock on the 4th day at 0, and sell the stock on the 5th day at 1. Profit is 1.
    Total profit is 2.

Example 2:
Input: [4, 3, 2, 1]
Output: 0
Explanation: No transaction, profit is 0.
"""

"""
Solution: DP. Use buy to record the max profit left after a purchase when you do not have stock in hand (after selling).
Use sell to record the max profit after a buy. 
"""
from typing import (
    List,
)

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def max_profit(self, prices: List[int]) -> int:
        # write your code here
        if not prices:
            return 0
        buy, sell = -prices[0], 0
        for price in prices:
            buy = max(buy, sell - price)
            sell = max(sell, price + buy)
        return sell
    
"""
Time Complexity: O(n)
Space Complexity: O(1)
"""