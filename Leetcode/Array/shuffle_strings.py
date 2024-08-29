from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        new = [''] * n
        for i in range(n):
            new[indices[i]] = s[i]
        return "".join(new)
