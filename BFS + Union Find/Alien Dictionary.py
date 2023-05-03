"""
Description
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.
You may assume all letters are in lowercase.
The dictionary is invalid, if string a is prefix of string b and b is appear before a.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return the smallest in normal lexicographical order.
The letters in one string are of the same rank by default and are sorted in Human dictionary order.

Example 1:
Input：["wrt","wrf","er","ett","rftt"]
Output："wertf"
Explanation：
from "wrt"and"wrf" ,we can get 't'<'f'
from "wrt"and"er" ,we can get 'w'<'e'
from "er"and"ett" ,we can get 'r'<'t'
from "ett"and"rftt" ,we can get 'e'<'r'
So return "wertf"

Example 2:
Input：["z","x"]
Output："zx"
Explanation：
from "z" and "x"，we can get 'z' < 'x'
So return "zx"
"""
"""
Solution: Topological Sorting with heapq. 
Because it asks to output the order in human dictionary order when there is more than one letter in the queue whose indegree = 0.
"""
import heapq
class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alien_order(self, words: List[str]) -> str:
        # Write your code here
        graph, indegree = self.build_graph_indegree(words)
        if not graph:
            return ""
        queue = []
        result = []
        n = 0
        for key, val in indegree.items():
            if val == 0:
                heapq.heappush(queue, key)
        
        while queue:
            head = heapq.heappop(queue)
            result.append(head)
            n += 1
            for neighbor in graph[head]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    heapq.heappush(queue, neighbor)
        return "".join(x for x in result) if n == len(graph) else ""
    
    def build_graph_indegree(self, words):
        graph = {}
        indegree = {}
        for word in words:
            for c in word:
                if c not in graph:
                    graph[c] = []
                if c not in indegree:
                    indegree[c] = 0
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    graph[word1[j]].append(word2[j])
                    indegree[word2[j]] += 1 
                    break 
                if j == min(len(word1), len(word2)) - 1:
                    if len(word1) > len(word2):
                        return None, None

        return graph, indegree