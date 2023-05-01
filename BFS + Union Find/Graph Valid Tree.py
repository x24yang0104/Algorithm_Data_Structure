"""
Description
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1:
Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true.

Example 2:
Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: false.
"""

"""
Solution 1: BFS from any node, check if it could visit all nodes 
"""
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # write your code here
        visited = set()
        neighbors, count_edges =  self.get_neighbors(n, edges)
        if count_edges != n - 1:
            return False
        queue = []
        queue.append(0)
        visited.add(0)
        while queue:
            node = queue.pop(0)
            for neighbor in neighbors[node]:
                if neighbor in visited:
                    continue
                queue.append(neighbor)
                visited.add(neighbor)
        return len(visited) == n
    
    def get_neighbors(self, n:int, edges: List[List[int]]):
        neighbors = {x:[] for x in range(n)}
        count = 0
        for edge in edges:
            neighbors[edge[1]].append(edge[0])
            neighbors[edge[0]].append(edge[1])
            count += 1
        return neighbors, count
    
"""
Solution 2: Union Find to see if there is only one block
"""
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # write your code here
        if len(edges) != n - 1:
            return False
        self.count = n
        self.father = [i for i in range(n)]
        for edge in edges:
            self.union(edge[0], edge[1])
        return self.count == 1
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return
        self.father[root_a] = root_b
        self.count -= 1
    
    def find(self, a):
        root_a = self.father[a]
        if a == root_a:
            return a
        self.father[a] = self.find(root_a)
        return self.father[a]
    


