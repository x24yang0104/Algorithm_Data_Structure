"""
Description
Give a dictionary of words and a sentence with all whitespace removed, return the number of sentences you can form by inserting whitespaces to the sentence so that each word can be found in the dictionary.
Ignore case
Sentence is not empty

Example1
Input:
"CatMat"
["Cat", "Mat", "Ca", "tM", "at", "C", "Dog", "og", "Do"]
Output: 3
Explanation:
we can form 3 sentences, as follows:
"CatMat" = "Cat" + "Mat"
"CatMat" = "Ca" + "tM" + "at"
"CatMat" = "C" + "at" + "Mat"

Example2
Input:
"a"
[]
Output: 
"""

"""
Solution 1: DFS + Memoization
"""
class Solution:
    """
    @param s: A string
    @param dict: A set of word
    @return: the number of possible sentences.
    """
    def word_break3(self, s: str, dict: Set[str]) -> int:
        # Write your code here
        s = s.lower()
        dict_low = set(x.lower() for x in dict)
        return self.dfs(s, dict_low, {})

    def dfs(self, s, dict, memo):
        if s in memo:
            return memo[s]
        if len(s) == 0:
            return 1
        result = 0
        for i in range(1, len(s) + 1):
            if s[:i] not in dict:
                continue
            result += self.dfs(s[i:], dict, memo)
        memo[s] = result
        return result

"""
Time Complexity: O(n^2)
Space Complexity: O(n)
"""

"""
Solution 2: DP
"""
class Solution:
    """
    @param s: A string
    @param dict: A set of word
    @return: the number of possible sentences.
    """
    def word_break3(self, s: str, dict: Set[str]) -> int:
        # Write your code here
        n = len(s)
        dp = [0 for _ in range(n + 1)]
        s = s.lower()
        dict = set(x.lower() for x in dict)

        dp[0] = 1
        for i in range(1, n + 1) :
            for j in range(i):
                if s[j : i] in dict:
                    dp[i] += dp[j]
        return dp[n]
"""
Time Complexity: O(n^2)
Space Complexity: O(n)
"""



