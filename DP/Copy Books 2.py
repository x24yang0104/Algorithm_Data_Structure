"""
Description
Given n books and each book has the same number of pages. There are k persons to copy these books and the i-th person needs times[i] minutes to copy a book.

Each person can copy any number of books and they start copying at the same time. What's the best strategy to assign books so that the job can be finished at the earliest time?

Return the shortest time.

Example
Example 1:

Input: n = 4, times = [3, 2, 4]
Output: 4
Explanation: 
    First person spends 3 minutes to copy 1 book.
    Second person spends 4 minutes to copy 2 books.
    Third person spends 4 minutes to copy 1 book.
Example 2:

Input: n = 4, times = [3, 2, 4, 5]
Output: 4
Explanation: Use the same strategy as example 1 and the forth person does nothing.
"""

"""
Solution1: DP. we can define dp[i][j] means the minimus time needed for first i people copy first j books. dp[i][j] = min(dp[i - 1][j], max(dp[i - 1][j - 1], times[j - 1], max(dp[i - 1][j - 2], times[j - 1] * 2)...max(dp[i - 1][0], times[j - 1] * j))

"""

class Solution:
    """
    @param n: An integer
    @param times: an array of integers
    @return: an integer
    """
    def copy_books_i_i(self, n: int, times: List[int]) -> int:
        m = len(times)
        dp = [[float('inf') for _ in range(n + 1)] for _ in range(m + 1)]

        dp[0][0] = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for k in range(j + 1):
                    dp[i][j] = min(dp[i][j], max(dp[i - 1][j - k], times[i - 1] * k))
        return dp[m][n]
    
"""
Time Complexity: O(mn2)
Space Complexity: O(n2)
"""    

"""
Solution 2 : Binary Search.
"""
class Solution:
    """
    @param n: An integer
    @param times: an array of integers
    @return: an integer
    """
    def copy_books_i_i(self, n: int, times: List[int]) -> int:
        # write your code here
        if not times:
            return 0
        start = min(times)
        end = max(times) * n

        while start + 1 < end:
            mid = (start + end) // 2
            if self.check_copy(mid, n, times):
                end = mid
            else:
                start = mid
        
        if self.check_copy(start, n, times):
            return start
        return end
    
    def check_copy(self, within, books, times):
        count = 0
        for time in times:
            if time <= within:
                count += within // time
        if count >= books:
            return True
        return False














