"""
Description
Give a two-dimensional grid, each grid has a value, 2 for wall, 1 for zombie, 0 for human (numbers 0, 1, 2).Zombies can turn the nearest people(up/down/left/right) into zombies every day, but can not through wall. How long will it take to turn all people into zombies? Return -1 if can not turn all people into zombies.

Example 1:
Input:
[[0,1,2,0,0],
 [1,0,0,2,1],
 [0,1,0,0,0]]
Output:
2

Example 2:
Input:
[[0,0,0],
 [0,0,0],
 [0,0,1]]
Output:
4
"""
"""
Solution: BFS
"""

class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    def zombie(self, grid: List[List[int]]) -> int:
        # write your code here
        if not grid or not grid[0]:
            return -1
        
        queue = []
        m, n = len(grid), len(grid[0])
        people_count, day_count = 0, 0
        dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    people_count += 1
                elif grid[i][j] == 1:
                    queue.append((i, j))
                    
        if people_count == 0:
            return 0
        
        def inbound(x, y):
            return 0 <= x < m and 0 <= y < n
        
        while queue:
            day_count += 1
            size = len(queue)
            for k in range(size):
                x, y = queue[k]
                for i in range(len(dx)):
                    curr_dx, curr_dy = x + dx[i], y + dy[i]
                    if inbound(curr_dx, curr_dy) and grid[curr_dx][curr_dy] == 0:
                        grid[curr_dx][curr_dy] = 1
                        queue.append((curr_dx, curr_dy))
                        people_count -= 1
                        if people_count == 0:
                            return day_count         
            queue = queue[size:]       
        return -1
"""
Time Complexity: O(n) n is the number of nodes
Space Complexity: O(n) n is the number of nodes
"""