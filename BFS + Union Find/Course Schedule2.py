"""
Description
There are a total of n courses you have to take, labeled from 0 to n - 1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:
Input: n = 2, prerequisites = [[1,0]] 
Output: [0,1]

Example 2:
Input: n = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]] 
Output: [0,1,2,3] or [0,2,1,3]
"""

"""
Solution: Topological Sorting.
"""
class Solution:
    """
    @param num_courses: a total of n courses
    @param prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def find_order(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        # write your code here
        result = []
        if num_courses == 0:
            return result
        indegree = {x : 0 for x in range(num_courses)}
        neighbors= {x:[] for x in range(num_courses)}
        for prerequisite in prerequisites:
            indegree[prerequisite[0]] += 1
            neighbors[prerequisite[1]].append(prerequisite[0])
        queue = [x for x in indegree if indegree[x] == 0]
        while len(queue):
            course = queue.pop(0)
            result.append(course)
            for neighbor in neighbors[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return result

"""
Time Complexity: O(E + V)
Space Complexity: O(E + V)
"""