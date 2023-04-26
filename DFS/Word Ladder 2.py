"""
Description
Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end.

Transformation rule such that:
Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
All words have the same length.
All words contain only lowercase alphabetic characters.
At least one solution exists.
The number of words is less than or equal to 10000
The word length is less than or equal to 10

Example 1:
Input:
start = "a"
end = "c"
dict =["a","b","c"]

Output:
[["a","c"]]
"""

"""
Solution: BFS + DFS. It requires to genereate all possible paths. So we can do a BFS from the desination to caculate the distance level for each node to the desination. 
So when we do DFS, we only move 1 step near the desination. 
"""

class Solution:
    """
    @param start: a string
    @param end: a string
    @param dict: a set of string
    @return: a list of lists of string
             we will sort your return value in output
    """
    def find_ladders(self, start: str, end: str, dict: Set[str]) -> List[List[str]]:
        # write your code here
        dict.add(start)
        dict.add(end)
        word_step = self.word_step(end, start, dict)
        results = []
        self.dfs(start, end, set(), word_step, [start], results, dict)
        return results

    def dfs(self, start, end, visited, word_step, result, results, dict):
        if start == end:
            results.append(result[:])
            return
        for neighbor in self.get_neighbors(start, dict):
            if neighbor in visited:
                continue
            if word_step[neighbor] == word_step[start] - 1:
                result.append(neighbor)
                visited.add(neighbor)
                self.dfs(neighbor, end, visited, word_step, result, results, dict)
                visited.remove(neighbor)
                result.pop()

    def word_step(self, start, end, dict):
        word_step = {}
        level = 0
        queue = []
        visited = set()
        queue.append(start)
        visited.add(start)
        while queue:
            size = len(queue)
            for i in range(size):
                head = queue.pop(0)               
                word_step.update({head : level})
                for neighbor in self.get_neighbors(head, dict):
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)
                    visited.add(neighbor)
            level += 1
        
        return word_step

    def get_neighbors(self, word, dict):
        neighbors = []
        for i in range(len(word)):
            for replace in range(ord('a'), ord('z') + 1):
                if word[i] == chr(replace):
                    continue
                new_word = word[:i] + chr(replace) + word[i + 1:]
                if new_word in dict:
                    neighbors.append(new_word)
        return neighbors

"""
Time Complexity: O(N + 26 * M * N). To search in a graph, the time complexity is O(N + M) which N is the nodes of the graph and M is the edges of a graph.
For the question, there are n nodes in the dict, and for each nodes, there are at most 26*m edges where m is the longest word length.
Space Complexity: O(26 * M * N). For BFS, the maximum elements in queue is 26 * m * n and for DFS, the maximum result is also 26 * M * N
"""
