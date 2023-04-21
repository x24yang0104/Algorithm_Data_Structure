"""
Given a binary tree, find the maximum path sum.
The path may start and end at any node in the tree.
(Path sum is the sum of the weights of nodes on the path between two nodes.)

Example
Example 1:

Input:

tree = {2}
Output:

2
Explanation:

There is only one node 2
Example 2:

Input:

tree = {1,2,3}
Output:

6
Explanation:

As shown in the figure below, the longest path is 2-1-3
      1
     / \
    2   3

A tree node is defined like this:
class TreeNode:
  def __init__(self, val):
      self.val = val
      self.left, self.right = None, None
"""
"""
Solution: create a global variable to use update the max value. 
Define a DFS helper function which will return a node's max value you can get 
when it is one end so it could be used to connect its parent node.
"""
class Solution:
  def max_path_sum(self, root: TreeNode) -> int:
    self.max_val = float('-inf')
    self.dfs(root)
    return self.max_val
  
  def dfs(self, root: TreeNode) -> TreeNode:
    if not root:
      return float('-inf')
    #if its child is negtive, it is not gettin bigger to add this child, so we use 0 to filter it out
    #same for right child
    left = max(self.dfs(root.left), 0) 
    right = max(self.dfs(root.right), 0) 
    self.max_val = max(self.max_val, right + left + root.val)
    #return one side with root, so the root can be used to connect parent. 
    return max(root.val + left, root.val + right) 

"""
Time Complexity: O(n) this dfs only visit earch node one time, so the time is O(n) and n is the amount of nodes of the tree.  
Space Complexity: O(n) the space depends on the deepth of the recrusive, since a tree at most has n level, so the space is O(n)
"""

    
