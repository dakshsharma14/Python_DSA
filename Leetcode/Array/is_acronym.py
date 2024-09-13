"""
class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        count = 0
        new = []
        for i in range(len(words)):
            new.append(words[i][0])
        strings = "".join(new)
        if strings == s:
            return True
        else:
            return False

"""
from typing import List


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return "".join(word[0] for word in words) == s
