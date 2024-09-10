from collections import Counter
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        freq1 = Counter(s1.split())
        freq2 = Counter(s2.split())
        new = []
        for i in s1.split():
            if freq1[i] == 1 and freq2[i] == 0:
                new.append(i)
        for i in s2.split():
            if freq2[i] == 1 and freq1[i] == 0:
                new.append(i)

        return new
