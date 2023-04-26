"""
Description
Given a string, find all permutations of it without duplicates.

Example 1:
Input:
s = "abb"
Output:
["abb", "bab", "bba"]
Explanation:
There are six kinds of full arrangement of abb, among which there are three kinds after removing duplicates.

Example 2:
Input:
s = "aabb"
Output:
["aabb", "abab", "baba", "bbaa", "abba", "baab"]
"""

class Solution:
    """
    @param str: A string
    @return: all permutations
             we will sort your return value in output
    """
    def string_permutation2(self, str: str) -> List[str]:
        # write your code here
        s_array = sorted(str)
        results = []
        self.dfs(s_array, [], set(), results)
        return results

    def dfs(self, s_array, result, visited, results):
        if len(visited) == len(s_array):
            results.append("".join(result))
            return 
        
        for i in range(len(s_array)):
            if i in visited:
                continue
            if i != 0 and s_array[i] == s_array[i - 1] and i - 1 not in visited:
                continue
            result.append(s_array[i])
            visited.add(i)
            self.dfs(s_array, result, visited, results)
            visited.remove(i)
            result.pop()

"""
Time Complexity: O(S)，S means that in the search tree, the sum of all the possibole leaf node's deepth. Worse case, n * 2^n
Space Complexity: The space of dfs depends on the deepth of the stack. In this case, O(len(s)) is the worst case.
"""


