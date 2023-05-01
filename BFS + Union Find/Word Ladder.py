"""
Description
Given two words (start and end), and a dictionary, find the shortest transformation sequence from start to end, output the length of the sequence.
Transformation rule such that:
Only one letter can be changed at a time
Each intermediate word must exist in the dictionary. (Start and end words do not need to appear in the dictionary ))
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the dictionary.
You may assume beginWord and endWord are non-empty and are not the same.
len(dict)<=5000,len(start)<5

Example 1:
Input:
start = "a"
end = "c"
dict =["a","b","c"]
Output:
2
Explanation:
"a"->"c"

Example 2:
Input:
start ="hit"
end = "cog"
dict =["hot","dot","dog","lot","log"]
Output:
5
Explanation:
"hit"->"hot"->"dot"->"dog"->"cog"
"""

"""
BFS
"""
class Solution:
    """
    @param start: a string
    @param end: a string
    @param dict: a set of string
    @return: An integer
    """
    def ladder_length(self, start: str, end: str, dict: Set[str]) -> int:
        # write your code here
        count = 0
        dict.add(start)
        dict.add(end)
        queue = []
        visited = set()
        queue.append(start)

        while queue:
            size = len(queue)
            count += 1
            for _ in range(size):
                head = queue.pop(0)
                if head == end:
                    return count
                for neighbor in self.get_neighbor(head, dict):
                    if neighbor in visited:
                        continue 
                    queue.append(neighbor)
                    visited.add(neighbor)          
        return -1
    
    def get_neighbor(self, word, dict):
        neighbors = []
        for c in range(ord('a') , ord('z') + 1):
            for i in range(len(word)):
                if chr(c)  == word[i]:
                    continue
                word_new = word[:i] + chr(c) + word[i + 1:]
                if word_new in dict:
                    neighbors.append(word_new)
        return neighbors

"""
Time Complexity: O(NL^2)
Space Complexity: O(max(n, 25L))
"""
