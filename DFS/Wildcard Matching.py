"""
Description
Given an input string s and a pattern p, implement wildcard pattern matching with support for '?' and '*'. The matching rules are as follows：

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Wechat reply 【Two Sigma】 get the latest requent Interview questions. (wechat id : jiuzhang1104)


0 <= |s|, |p| <= 1000
It is guaranteed that s only contains lowercase English letters and p contains lowercase English letters , ? and *

Example
Example 1

Input:
"aa"
"a"
Output: false
Example 2

Input:
"aa"
"aa"
Output: true
Example 3

Input:
"aaa"
"aa"
Output: false
Example 4

Input:
"aa"
"*"
Output: true
Explanation: '*' can replace any string
Example 5

Input:
"aa"
"a*"
Output: true
Example 6

Input:
"ab"
"?*"
Output: true
Explanation: '?' -> 'a' '*' -> 'b'
Example 7

Input:
"aab"
"c*a*b"
Output: false
"""

"""
Solution 1: DFS + memeioziation. One case is that the s[0] == p[0] or p[0] == ?, then dfs(s[1:], p[1:]). The other case is
the s[0] == *, then dfs(s[1:], p) or dfs(s, p[1:])
"""

class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def is_match(self, s: str, p: str) -> bool:
        # write your code here
        if self.only_star(p):
            return True
        return self.dfs(s, p, {})

    def dfs(self, s, p, memo):
        if (s, p) in memo:
            return memo[(s, p)]        
        if len(s) == 0:
            return len(p) == 0 or self.only_star(p)
        if len(p) == 0:
            return len(s) == 0

        result = False
        s1, p1 = s[0], p[0]
        if p1 == "?" or s1 == p1:
            result = self.dfs(s[1:], p[1:], memo)
        elif p1 == "*":
            result = self.dfs(s[1:], p, memo) or self.dfs(s, p[1:], memo)

        memo[(s, p)] = result
        return result
    
    def only_star(self, str):
        for c in str:
            if c != "*":
                return False
        return True