"""
Description
Say you have an array for which the ith element is the price of a given stock on day i.

Example 1
Input: [3, 2, 3, 1, 2]
Output: 1
Explanation: You can buy at the third day and then sell it at the 4th day. The profit is 2 - 1 = 1

Example 2
Input: [1, 2, 3, 4, 5]
Output: 4
Explanation: You can buy at the 0th day and then sell it at the 4th day. The profit is 5 - 1 = 4

Example 3
Input: [5, 4, 3, 2, 1]
Output: 0
Explanation: You can do nothing and get nothing.
"""

"""
Solution: DP. Use buy to record the min buy price, and Use sell to record the max profit. Loop the array one time.
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
        buy, sell = -prices[0], 0
        for price in prices:
            buy =  max(-price, buy)
            sell = max(sell, price + buy)
        return sell

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""