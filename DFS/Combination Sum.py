"""
Description
Given a set of candidate numbers candidates and a target number target. Find all unique combinations in candidates where the numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.
All numbers (including target) will be positive integers.
Numbers in a combination a1, a2, … , ak must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak)
Different combinations can be in any order.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [2, 3, 6, 7], target = 7
Output: [[7], [2, 2, 3]]

Example 2:
Input: candidates = [1], target = 3
Output: [[1, 1, 1]]
"""

"""
Solution: DFS. 
"""
class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
             we will sort your return value in output
    """
    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        # write your code here
        results = []
        self.dfs(sorted(candidates), 0, [], results, target)
        return results
    
    def dfs(self, nums, start, result, results, target):
        if target == 0:
            results.append(result[:])
            return 
        if target < 0:
            return
        for i in range(start, len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            result.append(nums[i])
            self.dfs(nums, i, result, results, target - nums[i])
            result.pop()
"""
Time Complexity: O(S)，S means that in the search tree, the sum of all the possibole leaf node's deepth.
Space Complexity: The space of dfs depends on the deepth of the stack. In this case, O(target) is the worst case.
"""
