"""
Description
Given an directed graph, a topological order of the graph nodes is defined as follow:
For each directed edge A -> B in graph, A must before B in the order list.
The first node in the order can be any node in the graph with no nodes direct to it.
Find any topological order for the given graph.
You can assume that there is at least one topological order in the graph.
Learn more about representation of graphs
The number of graph nodes <= 5000

Example 1:
Input:
graph = {0,1,2,3#1,4#2,4,5#3,4,5#4#5}
Output:
[0, 1, 2, 3, 4, 5]
Explanation:
The topological order can be:
[0, 1, 2, 3, 4, 5]
[0, 2, 3, 1, 5, 4]
...
You only need to return any topological order for the given graph.
Challenge
Can you do it in both BFS and DFS?
"""

"""
Solution 1: BFS
"""
class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        indegree = self.get_indegree(graph)
        queue = []
        order = []
        visited = set()
        for node in indegree:
            if indegree[node] == 0:
                queue.append(node)
                visited.add(node)
        while queue:
            head = queue.pop(0)
            order.append(head)
            for neighbor in head.neighbors:
                if neighbor in visited:
                    continue
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    visited.add(neighbor)
        return order

    def get_indegree(self, graph):
        indegree = {node : 0 for node in graph}
        for node in graph:
            for neighbor in node.neighbors:
                indegree[neighbor] += 1              
        return indegree
"""
Time Complexity: O(V + E) V is the node, and E is the edge
Space Complexity: O(V) V is the node.
"""
"""
Solution 2: DFS. Need to be noticed that, for dfs, after adding node to result, the indegree needs to minus one. Otherwise, it will be added again if it is the neighbor of the following nodes.
"""
class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        indegree = self.get_indegree(graph)
        top_sort = []
        for node in indegree:
            if indegree[node] == 0:
                self.dfs(indegree, node, top_sort)
        return top_sort
    
    def dfs(self, indegree, node, top_sort):
        top_sort.append(node)
        indegree[node] -= 1
        for neighbor in node.neighbors:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                self.dfs(indegree, neighbor, top_sort)


    def get_indegree(self, graph):
        indegree = {node : 0 for node in graph}
        for node in graph:
            for neighbor in node.neighbors:
                indegree[neighbor] += 1              
        return indegree

"""
Time Complexity: O(V + E) V is the node, and E is the edge
Space Complexity: O(V) V is the node.
"""