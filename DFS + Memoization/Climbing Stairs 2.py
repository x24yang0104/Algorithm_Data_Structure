"""
Description
A child is running up a staircase with n steps, and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.
For n=0, we think the answer is 1.
Example 1:
Input: 3
Output: 4
Explanation: 1 + 1 + 1 = 2 + 1 = 1 + 2 = 3 = 3 , there are 4 ways.

Example 2:
Input: 4
Output: 7
Explanation: 1 + 1 + 1 + 1 = 1 + 1 + 2 = 1 + 2 + 1 = 2 + 1 + 1 = 2 + 2 = 1 + 3 = 3 + 1 = 4 , there are 7 ways.
"""

"""
Solution 1: DFS + memoization
"""

class Solution:
    """
    @param n: An integer
    @return: An Integer
    """
    def climb_stairs2(self, n: int) -> int:
        # write your code here
        return self.dfs(0, n, {})
    
    def dfs(self, curr, target, memo):
        if curr == target:
            return 1
        if curr in memo:
            return memo[curr]
        if curr > target:
            return 0
        left_1 = self.dfs(curr + 1, target, memo)
        left_2 = self.dfs(curr + 2, target, memo)
        left_3 = self.dfs(curr + 3, target, memo)
        result = left_1 + left_2 + left_3
        memo[curr] = result
        
        return result
    
"""
Time Complexity: O(n) 
Space Complexity: O(n)
"""

"""
Solution 2: DP, go out
"""
class Solution:
    """
    @param n: An integer
    @return: An Integer
    """
    def climb_stairs2(self, n: int) -> int:
        # write your code here
        if n == 0 or n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        for i in range(n):
            if i + 1 <= n:
                dp[i + 1] += dp[i]
            if i + 2 <= n:
                dp[i + 2] += dp[i]
            if i + 3 <= n:
                dp[i + 3] += dp[i] 
        return dp[n]
"""
Time Complexity: O(n) 
Space Complexity: O(n)
"""

"""
Solution 3: DP. Come from
"""
class Solution:
    """
    @param n: An integer
    @return: An Integer
    """
    def climb_stairs2(self, n: int) -> int:
        # write your code here
        if n < 2:
            return 1       
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        return dp[n]
    
"""
Time Complexity: O(n) 
Space Complexity: O(n)
"""