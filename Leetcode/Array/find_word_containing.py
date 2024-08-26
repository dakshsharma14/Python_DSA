from typing import List
"""
Tag : Array and string 
"""
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        word = []
        for i, c in enumerate(words):
            if x in c:
                word.append(i)
        return word
# or
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, c in enumerate(words) if x in c]