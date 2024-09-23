from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        new = []
        for i in range(len(words)):
            strings = words[i].split(separator)
            for j in range(len(strings)):
                if strings[j]:
                    new.append(strings[j])
        return new
