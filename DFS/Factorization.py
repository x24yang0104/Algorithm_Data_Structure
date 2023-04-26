"""
Description
A non-negative numbers can be regarded as product of its factors.
Write a function that takes an integer n and return all possible combinations of its factors.

Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combination.

Example1
Input: 8
Output: [[2,2,2],[2,4]]
Explanation:
8 = 2 x 2 x 2 = 2 x 4

Example2
Input: 1
Output: []
"""

"""
Solution: DFS. 
"""
class Solution:
   
  def get_factors(self, n: int) -> List[List[int]]:
    results = []
    self.dfs(2, n, [], results)
    return results
  
  def dfs(self, start, target, result, results):
    #if the result is not empty, it means that the result + target is one possible combination
    if result:
        results.append(result[:] + [target])
    # two square(target) is the maxiumum possible factors, because the bigger factor has been record when the small dfs starts with small factor and there is no duplicate 
    for i in range(start, int(math.sqrt(target)) + 1):
        if target % i != 0:
            continue
        result.append(i)
        self.dfs(i, target // i, result, results)
        result.pop()       

"""
Time complexity: The time complexity for DFS is the amount of the answer  * the time to get one answer O(nlongn)
Space complexity: The O(n)
"""