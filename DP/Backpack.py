"""
Description
Given n items with size m as an integer m denotes the size of a backpack. How full you can fill this backpack?
(Each item can only be selected once and the size of the item is a positive integer)

Example 1:
Input:
array = [3,4,8,5]
backpack size = 10
Output:
9
Explanation:
Load 4 and 5.

Example 2:
Input:
array = [2,3,5,7]
backpack size = 12
Output:
12
Explanation:
Load 5 and 7.
"""

"""
Solution: DP. dp[i][j] means if the first i items could make size j. 
"""
from typing import (
    List,
)

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param a: Given n items with size A[i]
    @return: The maximum size
    """
    def back_pack(self, m: int, a: List[int]) -> int:
        # write your code here
        n = len(a)
        dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = True

        for x in range(1, n + 1):
            for y in range(1, m + 1):
                dp[x][y] = dp[x - 1][y]
                if y >= a[x - 1]:
                    dp[x][y] = dp[x][y] or dp[x - 1][y - a[x - 1]]
                    
        result = float('-inf')
        for y in range(m + 1):
            if dp[n][y]:
                result = max(result, y)
        return result

"""
Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""

"""
How to optimize the space. Because dp[x][y] is decided by dp[x - 1][y] and dp[x - 1][y - a[x - 1]].
We can remove one demision to make dp[y] = dp[y] or dp[y - a[x - 1]]. However, we need to notice one thing is that if the code runs as the current sequence, the dp[y - a[x - 1]] will change first, and then we will not be able to get the correct value. 
Because we can only use one item once. If the smaller value is changed means that we have used the current item to make up the smaller value so that we can not use it again.
So we can run the second loop from the back to first. 
"""

from typing import (
    List,
)

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param a: Given n items with size A[i]
    @return: The maximum size
    """
    def back_pack(self, m: int, a: List[int]) -> int:
        # write your code here
        n = len(a)
        dp = [False for _ in range(m + 1)]
        dp[0] = True

        for x in a:
            for y in range(m, 0, -1):
                if y >= x:
                    dp[y] = dp[y] or dp[y - x]

        for y in range(m, -1, -1):
            if dp[y]:
                return y
        return -1
"""
Time Complexity: O(n^2)
Space Complexity: O(n)
"""

"""
Solution 2: DP. dp[i][j] means that the maximum size that could be filled by using the first i item within the size j, 
"""
from typing import (
    List,
)

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param a: Given n items with size A[i]
    @return: The maximum size
    """
    def back_pack(self, m: int, a: List[int]) -> int:
        # write your code here
        n = len(a)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= a[i - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - a[i - 1]] + a[i - 1])

        return dp[n][m]
"""
Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""
"""
How to optimize: similar to the above, remove one dimision to make dp[y] = max(dp[y], dp[y - weight] + weight). 
And we need to loop the size from big to small which means that the current item has not been used to make the smaller size.
"""
from typing import (
    List,
)

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param a: Given n items with size A[i]
    @return: The maximum size
    """
    def back_pack(self, m: int, a: List[int]) -> int:
        # write your code here
        n = len(a)
        dp = [0 for _ in range(m + 1)]

        for x in a:
            for j in range(m, 0, -1):
                if j >= x:
                    dp[j] = max(dp[j], dp[j - x] + x)

        return dp[m]
"""
Time Complexity: O(n^2)
Space Complexity: O(n)
"""