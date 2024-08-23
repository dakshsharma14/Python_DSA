"""
https://leetcode.com/problems/valid-parentheses/description/

"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if stack:
                    if mapping[c] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        # JUST TO MAKE SURE THE STACK IS EMPTY
        return len(stack) == 0
