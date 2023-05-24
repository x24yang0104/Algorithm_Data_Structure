"""
Description
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.
Return all such possible sentences.

Example 1:
Input："lintcode"，["de","ding","co","code","lint"]
Output：["lint code", "lint co de"]
Explanation：
insert a space is "lint code"，insert two spaces is "lint co de".

Example 2:
Input："a"，[]
Output：[]
Explanation：dict is null.
"""

"""
Solution: DFS + Memozation
"""

class Solution:
    """
    @param s: A string
    @param word_dict: A set of words.
    @return: All possible sentences.
             we will sort your return value in output
    """
    def word_break(self, s: str, word_dict: Set[str]) -> List[str]:
        # write your code here
        if not word_dict or not s:
            return []
        
        return self.dfs(s, word_dict, {})
    
    def dfs(self, s, word_dict, memo):
        if s in memo:
            return memo[s]

        if len(s) == 0:
            return []

        results = []   
        if s in word_dict:
            results.append(s)
            
        max_length = self.get_max_length(word_dict)
        for x in range(1, len(s)):
            prefix = s[:x]
            if len(prefix) > max_length:
                break
            if prefix not in word_dict:
                continue
            post = self.dfs(s[x:], word_dict, memo)
            for p in post:
                results.append(prefix + " "+ p) 
        memo.update({s: results})
        return results
    
    def get_max_length(self, word_dict):
        length = 0
        for word in word_dict:
            length = max(length, len(word))
        return length

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
    @param word_dict: A set of words.
    @return: All possible sentences.
             we will sort your return value in output
    """
    def word_break(self, s: str, word_dict: Set[str]) -> List[str]:
        # write your code here
        n = len(s)
        dp = [[] for _ in range(n + 1)]
        s = s.lower()
        word_dict = set(x.lower() for x in word_dict)
        max_length = self.get_max_length(word_dict)
        dp[0] = [""]
        for i in range(1, n + 1) :
            for j in range(i - 1, -1, -1):
                if i - j > max_length:
                    break
                if s[j : i] in word_dict:
                    for r in dp[j]:
                        dp[i].append(r.strip() + " "+ s[j : i])
        return dp[n]

    def get_max_length(self, word_dict):
        length = 0
        for word in word_dict:
            length = max(length, len(word))
        return length
"""
Time Complexity: O(n^2)
Space Complexity: O(n)
"""