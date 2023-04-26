"""
Description
Given n distinct positive integers, the integer k (1<=k<=n) and a target number.
Find k distinct numbers within these n numbers such that the sum of these k numbers equals the target number, and you need to find all the solutions that satisfy the requirement (the order of the solutions is not required).

Example 1:
Input:
array = [1,2,3,4]
k = 2
target = 5
Output:
[[1,4],[2,3]]
Explanation:
1+4=5,2+3=5

Example 2:
Input:
array = [1,3,4,6]
k = 3
target = 8
Output:
[[1,3,4]]
Explanation:
1+3+4=8
"""

"""
Solution: DFS
"""

class Solution:
    """
    @param a: an integer array
    @param k: a postive integer <= length(A)
    @param target: an integer
    @return: A list of lists of integer
             we will sort your return value in output
    """
    def k_sum_i_i(self, a: List[int], k: int, target: int) -> List[List[int]]:
        # write your code here
        results = []
        self.dfs(a, 0, k, target, [], results)
        return results
    
    def dfs(self, nums, start, k, target, result, results):
        if target < 0 or k < 0:
            return

        if target == 0 and k == 0:
            results.append(result[:])
            return 
        
        for i in range(start, len(nums)):
            result.append(nums[i])
            self.dfs(nums, i + 1, k - 1, target - nums[i], result, results)
            result.pop()
"""
Time Complexity: O(S), S means the sum of all leaf node's deepth in the search tree. Worse Case: n * 2pow(n)
Space complexity: O(k). 
"""
