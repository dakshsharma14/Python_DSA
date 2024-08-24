"""

"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # initial assumption that none of the elements of the string satisfy
        is_ok = [0] * len(s)
        stack = []

        """
        enumerate
        l1 = ["eat", "sleep", "repeat"]
        output : [(0, 'eat'), (1, 'sleep'), (2, 'repeat')]
        """
        for i, c in enumerate(s):
            if c == "(":
                # adding the index of the element
                stack.append(i)
            elif c == ")":
                if stack:
                    is_ok[stack.pop()] = 1
                    is_ok[i] = 1
                else:
                    continue
            else:
                continue

        ans = ""

        for i, c in enumerate(s):
            if c in "()":
                if is_ok[i]:
                    ans += c
                else:
                    pass
            else:
                ans += c

        return ans
