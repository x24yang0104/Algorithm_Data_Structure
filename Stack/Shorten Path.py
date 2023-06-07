"""
Description
Given an absolute path for a file (Unix-style), simplify it.
In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the directory up a level.
The result must always begin with /, and there must be only a single / between two directory names. The last directory name (if it exists) must not end with a trailing /. Also, the result must be the shortest string representing the absolute path.

Did you consider the case where path is "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".

Example 1:
Input: "/home/"
Output: "/home"

Example 2:
Input: "/a/./../../c/"
Output: "/c"
Explanation: "/" has no parent directory, so "/../" equals "/".
"""

"""
Solution: Stack. ".." pop, "." or "" skip, and then connect
"""

class Solution:
    """
    @param path: the original path
    @return: the simplified path
    """
    def simplify_path(self, path: str) -> str:
        # write your code here
        items = path.split("/")
        stack = []
        for item in items:
            if item == "..":
                if stack:
                    stack.pop()
            elif item == "." or not item:
                continue
            else:
                stack.append(item)
        return "/" + "/".join(stack)
    
"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
                
