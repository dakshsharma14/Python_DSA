"""
https://www.interviewbit.com/problems/redundant-braces/
nput: str = “((a+b))”
Output: YES
Explanation: ((a+b)) can reduced to (a+b), this Redundant

Input: str = “(a+(b)/c)”
Output: YES
Explanation: (a+(b)/c) can reduced to (a+b/c) because b is surrounded by () which is redundant.
"""
class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        stack = []
        for c in A:
            if c != ")":
                stack.append(c)
            else:
                count = 0
                while stack[-1] != "(":
                    popped = stack.pop()
                    if popped in "+-*/": count +=1
                stack.pop()

                if count == 0:
                    return 1

        return 0

