"""
Description
Find connected component in undirected graph.
Each node in the graph contains a label and a list of its neighbors.
(A connected component of an undirected graph is a subgraph in which any two vertices are connected to each other by paths, and which is connected to no additional vertices in the supergraph.)
You need return a list of label set.
Nodes in a connected component should sort by label in ascending order. Different connected components can be in any order.
Learn more about representation of graphs

Example 1:
Input: {1,2,4#2,1,4#3,5#4,1,2#5,3}
Output: [[1,2,4],[3,5]]
Explanation:

  1------2  3
   \     |  | 
    \    |  |
     \   |  |
      \  |  |
        4   5

Example 2:
Input: {1,2#2,1}
Output: [[1,2]]
Explanation:
  1--2
"""

"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """
    def connectedSet(self, nodes: List[UndirectedGraphNode]) -> List[List[int]]:
        # write your code here
        result = []
        visited = set()
        for node in nodes:
            if node in visited:
                continue    
            result.append(self.bfs(node, visited))
        return result
    
    def bfs(self, node, visited):
        result = []
        queue = []
        queue.append(node)
        visited.add(node)
        while queue:
            head = queue.pop(0)
            result.append(head.label)
            for neighbor in head.neighbors:
                if neighbor in visited:
                    continue
                queue.append(neighbor)
                visited.add(neighbor)
        return sorted(result)