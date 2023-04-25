"""
Description
Given a digit string excluded 0 and 1, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

'2': ['a', 'b', 'c']
'3': ['d', 'e', 'f']
'4': ['g', 'h', 'i']
'5': ['j', 'k', 'l']
'6': ['m', 'n', 'o']
'7': ['p', 'q', 'r', 's']
'8': ['t', 'u', 'v']
'9': ['w', 'x', 'y', 'z'] 

Although the answer above is in lexicographical order, your answer could be in any order you want.

Example 1:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
Explanation: 
'2' could be 'a', 'b' or 'c'
'3' could be 'd', 'e' or 'f'

Example 2:
Input: "5"
Output: ["j", "k", "l"]
"""

"""
Solution: DFS
"""

class Solution:
    """
    @param digits: A digital string
    @return: all possible letter combinations
             we will sort your return value in output
    """
    def letter_combinations(self, digits: str) -> List[str]:
        # write your code here
        dict = {}
        dict.update({'2': ['a', 'b', 'c']})
        dict.update({'3': ['d', 'e', 'f']})
        dict.update({'4': ['g', 'h', 'i']})
        dict.update({'5': ['j', 'k', 'l']})
        dict.update({'6': ['m', 'n', 'o']})
        dict.update({'7': ['p', 'q', 'r', 's']})
        dict.update({'8': ['t', 'u', 'v']})
        dict.update({'9': ['w', 'x', 'y', 'z']})        
        return self.dfs(digits, dict)
    
    def dfs(self, digits, dict):
        if not digits:
            return []
        result = []
        d = digits[0]
        for letter in dict[d]:
            posts = self.dfs(digits[1:], dict)
            if not posts:
                result.append(letter)
            else:
                for post in posts:
                    result.append(letter + post)
        return result
    
"""
Time Complexity: O(4^n), n is the length of input string, because for each string, there are at most 4 selections
Space Complexity: O(4^n), because at most, the result need O(4^n) to save the results
"""