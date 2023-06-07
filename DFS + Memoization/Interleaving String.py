"""
Description
Given three strings: s1, s2, s3, determine whether s3 is formed by the interleaving of s1 and s2.
len(s1),len(s2),len(s3)<500

Example 1:
Input:
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
Output:
true
Explanation:
s3 can be formed by the intersection of s1 and s2.

Example 2:
Input:
s1 = ""
s2 = ""
s3 = "1"
Output:
false
Explanation:
s3 cannot be formed by the intersection of s1 and s2.

Example 3:
Input:
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
Output:
false
Explanation:
s3 cannot be formed by the intersection of s1 and s2.

Challenge: O(n^2) time or better
"""

"""
Solution 1: dp. 
"""
class Solution:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """
    def is_interleave(self, s1: str, s2: str, s3: str) -> bool:
        # write your code here
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l3 != l1 + l2:
            return False

        dp = [[False for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        dp[0][0] = True
        for i in range(1, l1 + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for i in range(1, l2 + 1):
            dp[0][i] = dp[0][i - 1] and s2[i - 1] == s3[i - 1]

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                dp[i][j] = (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]) or (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1])
        
        return dp[l1][l2]
"""
Time Complexity: O(l1 * l2)
Space Complexity: O(l1 * l2)
"""

"""
Solution 2: DFS + memoization
"""
class Solution:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """
    def is_interleave(self, s1: str, s2: str, s3: str) -> bool:
        # write your code here
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l3 != l1 + l2:
            return False
        return self.dfs(s1, s2, s3, {})
    
    def dfs(self, s1, s2, s3, memo):
        if (s1, s2, s3) in memo:
            return memo[(s1, s2, s3)]
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3
        result = False
        if s1[0] == s3[0]:
            if self.dfs(s1[1:], s2, s3[1:], memo):
                result = True
        memo[(s1[1:], s2, s3[1:])] = result
        if s2[0] == s3[0]:
            if self.dfs(s1, s2[1:], s3[1:], memo):
                result = True
        memo[(s1, s2[1:], s3[1:])] = result
        return result
        
"""
Time Complexity: O(l1 * l2), the worst case, it goes to all combnation of l1 * l2
Space Complexity: O(l1 * l2), for the memo, the space is l1 * l2
"""




