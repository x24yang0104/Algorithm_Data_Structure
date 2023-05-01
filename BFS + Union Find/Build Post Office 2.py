"""
Description
Given a 2D grid, each cell is either a wall 2, an house 1 or empty 0 (the number zero, one, two), find a place to build a post office so that the sum of the distance from the post office to all the houses is smallest.
Returns the sum of the minimum distances from all houses to the post office.Return -1 if it is not possible.
You cannot pass through wall and house, but can pass through empty.
You only build post office on an empty.

Example 1:
Input：[[0,1,0,0,0],[1,0,0,2,1],[0,1,0,0,0]]
Output：8
Explanation： Placing a post office at (1,1), the distance that post office to all the house sum is smallest.

Example 2:
Input：[[0,1,0],[1,0,1],[0,1,0]]
Output：4
Explanation： Placing a post office at (1,1), the distance that post office to all the house sum is smallest.
"""

"""
Solution BFS: 
Trick 1: to copy 2D array in Python, import copy and run copy.deepcopy. Otherwise, only grid[0] is copyed
Trick 2: Some house 1 might not be able to reach some empty 0. So remember to create a visited to sum how many
visits for this empty 0 from each house 1
"""

import copy

class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """
    def shortest_distance(self, grid: List[List[int]]) -> int:
        # write your code here
        n = len(grid)
        m = len(grid[0])
        distance = [[0 for _ in range(m)] for _ in range(n)]
        visited = [[0 for _ in range(m)] for _ in range(n)]
        ones = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ones.append((i, j))
                    distance[i][j] = float('inf')
                elif grid[i][j] == 2:
                    distance[i][j] = float('inf')
        total = len(ones)
        for one in ones:
            grid_copy = copy.deepcopy(grid)
            self.bfs(one, grid_copy, distance, visited)

        min_distance = float('inf')
        for i in range (n):
            for j in range(m):
                if visited[i][j] == total:
                    min_distance = min(min_distance, distance[i][j])
        return min_distance if min_distance != float('inf') else -1
    
    def bfs(self, start, grid, distance, visited):
        n = len(grid)
        m = len(grid[0])
        direct_x, direct_y = (0, 1, 0, -1),(-1, 0, 1, 0)
        queue = []
        step = 0
        queue.append(start)
        grid[start[0]][start[1]] = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                head = queue.pop(0)
                x, y = head[0], head[1]               
                distance[x][y] += step
                visited[x][y] += 1
                for i in range(4): 
                    x_n, y_n = x + direct_x[i], y + direct_y[i]
                    if x_n >= 0 and x_n < n and y_n >= 0 and y_n < m and grid[x_n][y_n] == 0:
                        queue.append((x_n, y_n))
                        grid[x_n][y_n] = 1
            step += 1

"""
Time Complexity: O(k * n) k is the number of hosue 1. n is the total number of empty 0
Space Complexity: O(n) n is the total number in matrix
"""
