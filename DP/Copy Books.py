"""
Description
Given n books and the i-th book has pages[i] pages. There are k persons to copy these books.
These books list in a row and each person can claim a continous range of books. For example, one copier can copy the books from i-th to j-th continously, but he can not copy the 1st book, 2nd book and 4th book (without 3rd book).
They start copying books at the same time and they all cost 1 minute to copy 1 page of a book. What's the best strategy to assign books so that the slowest copier can finish at earliest time?
Return the shortest time that the slowest copier spends.
The sum of book pages is less than or equal to 2147483647

Example 1:

Input: pages = [3, 2, 4], k = 2
Output: 5
Explanation: 
    First person spends 5 minutes to copy book 1 and book 2.
    Second person spends 4 minutes to copy book 3.

Example 2:
Input: pages = [3, 2, 4], k = 3
Output: 4
Explanation: Each person copies one of the books.
Challenge
O(nk) time
"""

"""
Solution1: DP. Use dp[i][j] defines as the shorted time need for first i people to copy first j books. The dp transimission is dp[i][j] = min(dp[i - 1][1] + pages[1:j], dp[i - 1][2][2:j] +..... dp[i - 1][j - 1] + pages[j - 1: j])
"""

class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copy_books(self, pages: List[int], k: int) -> int:
        n = len(pages)
        dp = [[float('inf') for _ in range(n + 1)] for _ in range(k + 1)]
        dp[0][0] = 0

        for i in range(1, k + 1):
            for j in range(1, n + 1):
                count = 0
                for m in range(j - 1, -1, -1):
                    count += pages[m]
                    dp[i][j] = min(dp[i][j], max(dp[i - 1][m], count))

        return dp[k][n]

"""
Time complexity: O(n2k)
Space Complexity: O(nk)

"""

"""
Solution2: Binary Search, lowbond is the max page in pages, upper bound is total number is the pages, search to see if k people could finish the copy
"""
class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copy_books(self, pages: List[int], k: int) -> int:
        # write your code here
        if not pages:
            return 0
        n = len(pages)
        start = max(pages)
        end = sum(pages)

        while start + 1 < end:
            mid = (start + end) // 2
            if self.check_copy(mid, k, pages):
                end = mid
            else:
                start = mid
        
        if self.check_copy(start, k, pages):
            return start
        return end

    def check_copy(self, time, people, pages):
        count = 0
        total = 0
        for page in pages:
            total += page
            if total > time:
                count += 1
                total = page           
        if total > 0:
            count += 1
        if count > people:
            return False
        return True
    
"""
Time Complexity: O(nlogsum(pages))
Space Complexity: O(1)
"""

















