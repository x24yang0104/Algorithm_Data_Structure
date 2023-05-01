"""
Description
Given a 2D array representing the coordinates on the map, there are only values 0, 1, 2 on the map. value 0 means that it can pass, value 1 means not passable, value 2 means target place. Starting from the coordinates [0,0],You can only go up, down, left and right. Find the shortest path that can reach the destination, and return the length of the path.
The map must exist and is not empty, there is only one target. It is guaranteed targetMap[0][0]=0.

Example 1
Input:
[
 [0, 0, 0],
 [0, 0, 1],
 [0, 0, 2]
]
Output: 4
Explanation: [0,0] -> [1,0] -> [2,0] -> [2,1] -> [2,2]

Example 2
Input:
[
    [0,1],
    [0,1],
    [0,0],
    [0,2]
]
Output: 4
Explanation: [0,0] -> [1,0] -> [2,0] -> [3,0] -> [3,1]
"""

"""
Solution 1: BFS one direction
"""

class Solution:
    """
    @param target_map: 
    @return: 
    """
    def shortest_path(self, target_map: List[List[int]]) -> int:
        # Write your code here
        if not target_map:
            return False
        n = len(target_map)
        m = len(target_map[0])
        dirct_x = (1, 0, -1, 0)
        dirct_y = (0, 1, 0, -1)
        queue = []
        visited = set()
        queue.append((0, 0))
        visited.add((0, 0))
        
        distance = 0
        while queue:
            size = len(queue)
            distance += 1
            for _ in range(size):
                x, y = queue.pop(0)
                if target_map[x][y] == 2:
                    return distance - 1
                for i in range(4):
                    x_n = x + dirct_x[i]
                    y_n = y + dirct_y[i]
                    if x_n >= 0 and x_n < n and y_n >= 0 and y_n < m and (x_n, y_n) not in visited and target_map[x][y] != 1:
                        queue.append((x_n, y_n))
                        visited.add((x_n, y_n))
        return -1
    
"""
Time Complexity: O(n) n is the number of point
Space Complexity: O(n) n is the number of point
"""



