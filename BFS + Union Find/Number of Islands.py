"""
Description
Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.
Find the number of islands.

Example 1:
Input:
[
  [1,1,0,0,0],
  [0,1,0,0,1],
  [0,0,0,1,1],
  [0,0,0,0,0],
  [0,0,0,0,1]
]
Output:
3

Example 2:
Input:
[
  [1,1]
]
Output:
1
"""
"""
Solution 1. BFS
"""
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def num_islands(self, grid: List[List[bool]]) -> int:
        # write your code here
        if not grid:
            return 0
        n = len(grid)
        m = len(grid[0])
        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    self.bfs(grid, i, j)
                    count += 1
        
        return count
    
    def bfs(self, grid, i, j):
        direct_x = (0, 1, 0, -1)
        direct_y = (1, 0, -1, 0)
        n = len(grid)
        m = len(grid[0])
        queue = []
        queue.append((i, j))
        grid[i][j] = 0
        
        while queue:
            head = queue.pop()
            x, y = head[0], head[1] 
            for i in range(4):
                x_n, y_n = x + direct_x[i], y + direct_y[i]
                if x_n >= 0 and x_n < n and y_n >= 0 and y_n < m and grid[x_n][y_n] != 0:
                    queue.append((x_n, y_n))
                    grid[x_n][y_n] = 0

"""
Solution 2: Union Find. The number of island is the number of the connected block
"""
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def num_islands(self, grid: List[List[bool]]) -> int:
        # write your code here
        if not grid:
            return 0
        n = len(grid)
        m = len(grid[0])
        self.father = [i for i in range(m * n)]
        ones = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    ones.append((i, j))
        self.count = len(ones)
        direct_x = (1, 0, -1, 0)
        direct_y = (0, 1, 0, -1)
        for p in ones:
            i, j = p[0], p[1]
            for c in range(4):
                i_n, j_n = i + direct_x[c], j + direct_y[c]
                if i_n >= 0 and i_n < n and j_n >= 0 and j_n < m and grid[i_n][j_n] != 0:
                    self.union(i * m + j, i_n * m + j_n)
        return self.count

    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.count -= 1

    def find(self, a):
        root_a = self.father[a]
        if a == root_a:
            return a
        self.father[a] = self.find(root_a)
        return self.father[a]
    
"""
Time Complexity: O(N), N is the number of the numbers in the matrix. Because BFS will just do one loop to all nodes of a graph.
Space Complexity: O(N), the worst case for BFS will have N elements in the queue. Union find will need N for father array.
"""