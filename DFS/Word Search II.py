"""
Description
Given a matrix of lower alphabets and a dictionary. Find all words in the dictionary that can be found in the matrix. A word can start from any position in the matrix and go left/right/up/down to the adjacent position. One character only be used once in one word. No same word in dictionary

Example 1:
Input：["doaf","agai","dcan"]，["dog","dad","dgdg","can","again"]
Output：["again","can","dad","dog"]
Explanation：
  d o a f
  a g a i
  d c a n
search in Matrix，so return ["again","can","dad","dog"].

Example 2:
Input：["a"],["b"]
Output：[]
Explanation：
 a
search in Matrix，return [].

Challenge
Using trie to implement your algorithm.
"""

"""
Solution: DFS + Trie. Create a try and insert the words. Like the word search I which is using index to move forward, this question
use trie to move forward, if the surounding letter is not in current node's children, it will not keep searching. And to avoid the duplciate in results, when we find a word, we set the node.isWord = False and node.word = "" so it will not be found again.
"""

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
             we will sort your return value in output
    """
    def word_search_i_i(self, board: List[List[str]], words: List[str]) -> List[str]:
        # write your code here
        n, m = len(board), len(board[0])
        results = []
        trie = Trie()
        for word in words:
            trie.insert(word)
        for i in range(n):
            for j in range(m):
                if board[i][j] not in trie.root.children:
                    continue
                self.dfs(i, j, trie.root.children[board[i][j]], board, "", set([(i, j)]), results, trie)
        return [*set(results)]
    
    def dfs(self, x, y, node, board, result, visited, results, trie):
        n, m = len(board), len(board[0])
        direct_x, direct_y = (0, 1, 0, -1), (-1, 0, 1, 0)
        if node.isWord:
            results.append(node.word)
            node.isWord = False
            node.word = ""

        for i in range(4):
            x_n, y_n = x + direct_x[i], y + direct_y[i]
            if x_n >= 0 and x_n < n and y_n >= 0 and y_n < m and (x_n, y_n) not in visited and board[x_n][y_n] in node.children:
                visited.add((x_n, y_n))
                self.dfs(x_n, y_n, node.children[board[x_n][y_n]], board, result + board[x_n][y_n], visited, results, trie)
                visited.remove((x_n, y_n))

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True
        node.word = word

    def startWith(self, word):
        re = self.search(word)
        return re is not None

    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return None
            else:
                node = node.children[c]
        return node
            
class TrieNode:
    def __init__(self):
        self.isWord = False
        self.word = ""
        self.children = {}

"""
Time Complexity: O(nm * 4 * 26 ^ l) l is the longest word length in words
Space Complexity: O(l) we need l space to create trie, where l is all letters in the each word in words.
"""

