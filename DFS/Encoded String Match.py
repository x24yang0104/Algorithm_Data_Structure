"""
Given two strings, one of them is full string and the other is encoded. Oulput if these two strings matched. 
There may be mutiple numbers but each number has only 1 digit. 
for exmpale: 
datadog, d3dog -> True  
datadog, d2dog -> False
follow up:
What if the pattern has two digits number: d10dog
What if the pattern has some range: d{1,3}dog-> d1dog, d2dog, or d3dog 
What if the pattern has some skip character: d^4dog, '^' could match any character
What if the pattern has some universal character: d*dog, '*' could match any numbers of character
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
      print(str[j], pattern[i])
      if pattern[i].isdigit():
        j += int(pattern[i])      
      else:
        if pattern[i] != str[j]:
          return False
        j += 1
    return j == len(str)
solution = Solution()
print(solution.encoded_string_match("aaaa", "3"))    
    
