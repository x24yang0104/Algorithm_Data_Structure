"""
Description
Given a collection of integers that might contain duplicate numbers, return all possible subsets.
Each element in a subset must be in non-descending order.
The ordering between two subsets is free.
The solution set must not contain duplicate subsets.


Example 1:
Input:
nums = [0]
Output:
[
  [],
  [0]
]
Explanation:
The subsets of [0] are only [] and [0].

Example 2:
Input:
nums = [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
Explanation:
The distinct subsets of [1,2,2] are [], [1], [2], [1,2], [2,2], [1,2,2].

Challenge
Can you do it in both recursively and non-recursively?
"""
"""
Solution 1: DFS. Two different seearch tree
"""
class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
             we will sort your return value in output
    """
    def subsets_with_dup(self, nums: List[int]) -> List[List[int]]:
        # write your code here
        results = []
        self.dfs(sorted(nums), [], -1, 0, results)
        return results
    
    def dfs(self, nums, result, last, start, results):
        if start == len(nums):
            results.append(result[:])
            return
        if start != 0 and nums[start] == nums[start - 1] and start - 1 != last:
            self.dfs(nums, result, last, start + 1, results)
        else:
            result.append(nums[start])
            self.dfs(nums, result, start, start + 1, results)
            result.pop()
            self.dfs(nums, result, last, start + 1, results)

class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
             we will sort your return value in output
    """
    def subsets_with_dup(self, nums: List[int]) -> List[List[int]]:
        # write your code here
        results = []
        self.dfs(sorted(nums), [], 0, results)
        return results
    
    def dfs(self, nums, result, start, results):
        results.append(result[:])
        for i in range(start, len(nums)):
            if i != 0 and nums[i] == nums[i - 1] and i != start:
                continue
            result.append(nums[i])
            self.dfs(nums, result, i + 1, results)
            result.pop()
"""
Time Complextiy: O(n * 2^n) it takes n to copy result to results, and for each recursive, the has 2^n for the rest 
Space Complexity: O(n), the depth of the search tree is O(n) and for the result, the maximum one has n elements. So it is O(n)
"""

"""
Solution 2: BFS
"""

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
             we will sort your return value in output
    """
   def subsets_with_dup(self, nums: List[int]) -> List[List[int]]:
        # write your code here
        # write your code here
        nums.sort()
        results = []
        queue = []
        queue.append((0, [], 0))
        while queue:
            level, result, start = queue.pop(0)
            results.append(result)
            if level == len(nums):
                break
            for i in range(start, len(nums)):
                if i != 0 and nums[i] == nums[i - 1] and start != i:
                    continue
                queue.append((level, result + [nums[i]], i + 1))
            
        return results
    
"""
Time Complextiy: O(2^n), the queue maximum has 2^n elements, so pop all these elements took 2^n
Space Complexity: O(2^n), the queue maximum has 2^n elements, so the space is 2^n
""" 