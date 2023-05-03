"""
Given a knight in a chessboard n * m (a binary matrix with 0 as empty and 1 as barrier). the knight initialze position is (0, 0) and he wants to reach position (n - 1, m - 1), Knight can only be from left to right. Find the shortest path to the destination position, return the length of the route. Return -1 if knight can not reached.
If the knight is at (x, y), he can get to the following positions in one step:
(x + 1, y + 2)
(x - 1, y + 2)
(x + 2, y + 1)
(x - 2, y + 1)

Example 1:
Input:
[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
Output:
3
Explanation:
[0,0]->[2,1]->[0,2]->[2,3]

Example 2:
Input:
[[0,1,0],[0,0,1],[0,0,0]]
Output:
-1
"""
class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortest_path2(self, grid: List[List[bool]]) -> int:       
        # write your code here
        step = 0
        queue = []
        direct_x = (1, -1, 2, -2)
        direct_y = (2, 2, 1, 1)
        n, m = len(grid), len(grid[0])
        queue.append((0, 0))
        grid[0][0] = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                head = queue.pop(0)
                if head[0] == n - 1 and head[1] == m - 1:
                    return step
                for i in range(4):
                    n_x = head[0] + direct_x[i]
                    n_y = head[1] + direct_y[i]
                    if n_x >= 0 and n_x < n and n_y >= 0 and n_y < m and grid[n_x][n_y] != 1:
                        queue.append((n_x, n_y))
                        grid[n_x][n_y] = 1
            step += 1
        
        return -1
"""
Time Complexity: O(n) n is number of points
Space Complexity: O(n) n is number of points
"""