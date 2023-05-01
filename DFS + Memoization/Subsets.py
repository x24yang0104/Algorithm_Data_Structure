"""
Description
Given a set with distinct integers, return all possible subsets (in any order).
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
nums = [1,2,3] 
Output:
[ 
  [3], 
  [1], 
  [2], 
  [1,2,3], 
  [1,3], 
  [2,3], 
  [1,2], 
  [] 
] 
Explanation:
The subsets of [1,2,3] are [], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3].

Challenge
Can you do it in both recursively and non-recursively?
"""
"""
Sloution: DFS
"""
class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
             we will sort your return value in output
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # write your code here
        nums.sort()
        results = []
        self.dfs(nums, [], 0, results)
        return results
    
    def dfs(self, nums, result, start, results):
        results.append(result[:])
        for i in range(start, len(nums)):
            result.append(nums[i])
            self.dfs(nums, result, i + 1, results)
            result.pop()

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
             we will sort your return value in output
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # write your code here
        nums.sort()
        results = []
        self.dfs(nums, [], 0, results)
        return results
    
    def dfs(self, nums, result, start, results):
        if start == len(nums):
            results.append(result[:])
            return
        result.append(nums[start])
        self.dfs(nums, result, start + 1, results)
        result.pop()
        self.dfs(nums, result, start + 1, results)

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
    def subsets(self, nums: List[int]) -> List[List[int]]:
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
                queue.append((level, result + [nums[i]], i + 1))
            
        return results
    
"""
Time Complextiy: O(2^n), the queue maximum has 2^n elements, so pop all these elements took 2^n
Space Complexity: O(2^n), the queue maximum has 2^n elements, so the space is 2^n
""" 

    
