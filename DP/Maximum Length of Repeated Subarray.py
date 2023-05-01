"""Description
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.
1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100

Example 1:
Input:
[1,2,3,2,1]
[3,2,1,4,7]
Output:
3
Explanation:
The repeated subarray with maximum length is [3, 2, 1].

Example 2:
Input:
[1,2,3,4,5]
[6,7,8,9,10]
Output:
0
Explanation:
No repeated subarray.
"""
class Solution:
    """
    @param a: 
    @param b: 
    @return: return a integer 
    """
    def find_length(self, a: List[int], b: List[int]) -> int:
        # write your code here
        n, m = len(a), len(b)
        dp = [[0 for _ in range(m + 1)] for _ in range( n + 1)]
        max_val = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_val = max(max_val, dp[i][j])
                    
        return max_val
"""
Time complexity: O(m * n)
Space complexity: O(m * n)
"""