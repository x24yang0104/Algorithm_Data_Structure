"""
Description
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.
Example 1:
Input:
[
  [1, 0, 1, 0, 0],
  [1, 0, 1, 1, 1],
  [1, 1, 1, 1, 1],
  [1, 0, 0, 1, 0]
]
Output: 4

Example 2:
Input:
[
  [0, 0, 0],
  [1, 1, 1]
]
Output: 1
"""

"""
Solution: DP. 
"""

from typing import (
    List,
)

class Solution:
    """
    @param matrix: a matrix of 0 and 1
    @return: an integer
    """
    def max_square(self, matrix: List[List[int]]) -> int:
        # write your code here
        n, m = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for x in range(n):
          for y in range(m):
            if matrix[x][y] == 1:
                dp[x][y] = 1

        for x in range (1, n):
            for y in range(1, m):
                if matrix[x][y] == 0:
                    continue
                dp[x][y] = min(dp[x - 1][y], dp[x][y - 1], dp[x - 1][y - 1]) + 1
        result = 0
        for x in range(n):
            for y in range(m):
                result = max(result, dp[x][y])
        return result * result

"""
Time complexity: O(m * n)
Space Complexity: O(m * n)
"""

