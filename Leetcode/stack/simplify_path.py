# path :- https://leetcode.com/problems/simplify-path/description/


"""
start                   stack = []
directory up            stack.append(name)
directory down ..       stack.pop()
.                           -


Example 3:

Input: path = "/home/user/Documents/../Pictures"
split be like home, user, Documents, .., Pictures
Output: "/home/user/Pictures"

Explanation:

A double period ".." refers to the directory up a level.
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for directory in path.split("/"):
            # edge case as // , split gives empty
            if directory == "":
                pass
            if directory == ".":
                pass
            elif directory == "..":
                if stack:
                    stack.pop()
                else:
                    pass
            else:
                stack.append(directory)

        return "/" + "/".join(stack)


"""
faster in run time  as they are using the continue
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        toks = path.split("/")
        
        for tok in toks:
            
            if tok == "." or tok == "":
                continue

            if tok == "..":
                if not stack:
                    continue
                stack.pop()
                continue

            stack.append(tok)
        return '/' + '/'.join(stack)
"""