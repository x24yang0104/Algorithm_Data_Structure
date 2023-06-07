"""
Description
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
Example
Input : [4,4,6,1,1,4,2,5]
Output : 6
"""

"""
Solution: DP. Use buy1, buy2 to record the max profit after a purchase, initial value is the first price of the array. 
Use sell1, sell2 to record the max profit after each sell. Sell2 is the result. 
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
        buy1, buy2, sell1, sell2 = -prices[0], -prices[0], 0, 0
        for price in prices:
            buy1 = max(-price, buy1)
            sell1 = max(sell1, price + buy1)
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, price + buy2)
        return sell2

"""
Time Complexity: O(n)
Space Complexiyt: O(1)
"""