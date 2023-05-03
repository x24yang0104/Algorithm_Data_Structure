"""
Description
There are a total of n courses you have to take, labeled from 0 to n - 1.
Before taking some courses, you need to take other courses. For example, to learn course 0, you need to learn course 1 first, which is expressed as [0,1].
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
prerequisites may appear duplicated

Example 1:
Input: n = 2, prerequisites = [[1,0]] 
Output: true

Example 2:
Input: n = 2, prerequisites = [[1,0],[0,1]] 
Output: false
"""


"""
Solution: Topologic Sorting. Check if the topological sorting node count in queue is equal to the number of courses
"""

class Solution:
    """
    @param num_courses: a total of n courses
    @param prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def can_finish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        if num_courses == 0:
            return 
        count = 0
        indegree = {x : 0 for x in range(num_courses)}
        neighbors= {x:[] for x in range(num_courses)}
        for prerequisite in prerequisites:
            indegree[prerequisite[0]] += 1
            neighbors[prerequisite[1]].append(prerequisite[0])
        queue = [x for x in indegree if indegree[x] == 0]
        while len(queue):
            course = queue.pop(0)
            count += 1
            for neighbor in neighbors[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return count == num_courses
    

    """
    Time Complexity:O(V + E)
    Space Complexity: O(V + E)
    """