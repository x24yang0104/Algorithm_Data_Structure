"""
Description
Given a knight in a chessboard (a binary matrix with 0 as empty and 1 as barrier) with a source position, find the shortest path to a destination position, return the length of the route.
Return -1 if destination cannot be reached.
source and destination must be empty.
Knight can not enter the barrier.
Path length refers to the number of steps the knight takes.
If the knight is at (x, y), he can get to the following positions in one step:
(x + 1, y + 2)
(x + 1, y - 2)
(x - 1, y + 2)
(x - 1, y - 2)
(x + 2, y + 1)
(x + 2, y - 1)
(x - 2, y + 1)
(x - 2, y - 1)

Example 1:
Input:
[[0,0,0],
 [0,0,0],
 [0,0,0]]
source = [2, 0] destination = [2, 2] 
Output: 2
Explanation:
[2,0]->[0,1]->[2,2]

Example 2:
Input:
[[0,1,0],
 [0,0,1],
 [0,0,0]]
source = [2, 0] destination = [2, 2] 
Output:-1
"""

"""
Solution: BFS
"""

"""
Definition for a point:
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
"""

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortest_path(self, grid: List[List[bool]], source: Point, destination: Point) -> int:
        # write your code here
        step = 0
        queue = []
        direct_x = (1, 1, -1, -1, 2, 2, -2, -2)
        direct_y = (2, -2, 2, -2, 1, -1, 1, -1)
        n, m = len(grid), len(grid[0])
        queue.append(source)
        grid[source.x][source.y] = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                head = queue.pop(0)
                if head.x == destination.x and head.y == destination.y:
                    return step
                for i in range(8):
                    n_x = head.x + direct_x[i]
                    n_y = head.y + direct_y[i]
                    if n_x >= 0 and n_x < n and n_y >= 0 and n_y < m and grid[n_x][n_y] != 1:
                        queue.append(Point(n_x, n_y))
                        grid[n_x][n_y] = 1
            step += 1
        
        return -1
    
    """
    Time Complexity: O(n) n is number of points
    Space Complexity: O(n) n is number of points
    """