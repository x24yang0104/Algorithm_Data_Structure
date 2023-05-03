"""
Description
Given a matrix of lower alphabets and a dictionary. 
Find maximum number of words in the dictionary that can be found in the matrix at the same time. A word can start from any position in the matrix and go left/right/up/down to the adjacent position. 
One character only be used once in the matrix. No same word in dictionary

Example 1:
Input：
["doaf","agai","dcan"]，["dog","dad","dgdg","can","again"]
Output：
2
Explanation：
  d o a f
  a g a i
  d c a n
search in Matrix, you can find `dog` and `can` in the meantime.

Example 2:
Input：
["a"]，["b"]
Output：
0
Explanation：
 a
search in Matrix，return 0.
"""
"""
Solution: DFS + Trie. The difference with word search 2 is that finding a word, do not stop, keep searching for the following points which is the code:
for i in range(start_x, n):
    temp = 0
    if i == start_x:
        temp = start_y + 1
    for j in range(temp, m):
"""


class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: return the maximum nunber
    """
    def word_search_i_i_i(self, board: List[List[str]], words: List[str]) -> int:
        # write your code here
        n = len(board)
        m = len(board[0])
        self.total = 0
        trie = Trie()
        for word in words:
            trie.insert(word)
        for x in range(n):
            for y in range(m):
                if board[x][y] in trie.root.children:
                    self.dfs(board, trie, trie.root.children[board[x][y]], x, y, x, y, set([(x, y)]), set())
        return self.total

    def dfs(self, board, trie, node, start_x, start_y, x, y, visited, result):
        dire_x = [1, 0, -1, 0]
        dire_y = [0, 1, 0, -1]
        n = len(board)
        m = len(board[0])    

        if node.isEnd:
            result.add(node.word)
            self.total = max(self.total, len(result))
            node.isEnd = False        
            for i in range(start_x, n):
                temp = 0
                if i == start_x:
                    temp = start_y + 1
                for j in range(temp, m):
                    if (i, j) not in visited:
                        visited.add((i, j))
                        if board[i][j] in trie.root.children:
                            self.dfs(board, trie, trie.root.children[board[i][j]], i, j, i, j, visited, result)
                        visited.remove((i, j))
            result.remove(node.word)
            node.isEnd = True

        for i in range(4):
            n_x = x + dire_x[i]
            n_y = y + dire_y[i]
            if (n_x >=0 and n_x < n and n_y >=0 and n_y <m and (n_x, n_y) not in visited):
                if board[n_x][n_y] in node.children:
                    visited.add((n_x, n_y))
                    self.dfs(board, trie, node.children[board[n_x][n_y]], start_x, start_y, n_x, n_y, visited, result)
                    visited.remove((n_x, n_y))


class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True
        cur.word = word

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False