"""
Given two strings, one of them is full string and the other is encoded. Oulput if these two strings matched. 
There may be mutiple numbers but each number has only 1 digit. 
for exmpale: 
datadog, d3dog -> True  
datadog, d2dog -> False
"""

"""
Question 1: Two pointer
"""
class Solution:
  def encoded_string_match(self, str, pattern):
    if len(pattern) > len(str):
      return False
    j = 0
    for i in range(len(pattern)):
      if j >= len(str):
        return False
      if pattern[i].isdigit():
        j += int(pattern[i])      
      else:
        if pattern[i] != str[j]:
          return False
        j += 1
    return j == len(str)
  
"""
Time Complexity: O(n)
Space Complexity: O(1)
"""  
"""
follow up:
What if the pattern has two digits number: d10dog
What if the pattern has some range: d{1,3}dog-> d1dog, d2dog, or d3dog 
What if the pattern has some skip character: d^4dog, '^' could match any character
What if the pattern has some universal character: d*dog, '*' could match any numbers of character
"""
class Solution:
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
        if p1.isdigit():
            digit, length = self.get_digit(p)
            result = self.dfs(s[digit:], p[length:], memo)
        elif p1 == "{":
            start, end, length = self.get_range(p)
            for i in range(start, end + 1):
                result = result or self.dfs(s[i:], p[length:], memo)
        elif p1 == "^" or s1 == p1:
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

    def get_digit(self, pattern):
        i = 0
        while pattern[i].isdigit():
            i += 1
        return int(pattern[:i]), i

    def get_range(self, pattern):
        rng = pattern.index("}")
        nums = pattern[1 : rng]
        start, end = nums.split(",")
        return int(start), int(end), rng + 1

"""
Follow up solution 2: DP
"""
class Solution:
  def is_match(self, s: str, p: str) -> bool:
    # write your code here
    n = len(s)
    m = len(p)
    dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0][0] = True
    for j in range(1, m + 1):
        if p[j - 1] == "*":
            dp[0][j] = dp[0][j - 1]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if p[j - 1].isdigit():
                dijit, length = self.get_digit(p[j - 1:])
                if j - 2 >= 0 and p[j - 2].isdigit():
                    continue
                if i + dijit - 1 <= n and j + length - 1 <= m:
                    dp[i + dijit - 1][j + length - 1] = dp[i - 1][j - 1] 
            elif p[j - 1] == "{":
                start, end, length = self.get_range(p[j - 1:])
                for k in range(start, end + 1):
                    if i + k - 1 <= n and j + length - 1 <= m:
                        dp[i + k - 1][j + length - 1] = dp[i + k - 1][j + length - 1] or dp[i - 1][j - 1]
            elif s[i - 1] == p[j - 1] or p[j - 1] == "^":
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == "*":
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]    
    return dp[n][m]

  def get_digit(self, pattern):
      i = 0
      while pattern[i].isdigit():
          i += 1
      return int(pattern[:i]), i

  def get_range(self, pattern):
      rng = pattern.index("}")
      nums = pattern[1 : rng]
      start, end = nums.split(",")
      return int(start), int(end), rng + 1

solution = Solution()
print(solution.encoded_string_match("aaaa", "3"))    
    
