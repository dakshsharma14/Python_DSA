# class Solution:
#     def maximumNumberOfStringPairs(self, words: List[str]) -> int:
#         count = 0
#         for i in range(len(words)):
#             for j in range(i+1, len(words)):
#                 if words[i] == words[j][::-1]:
#                     count +=1
#         return count
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        seen = set()
        count = 0
        for word in words:
            reversed_word = word[::-1]  # Reverse the current word
            if reversed_word in seen:
                count += 1  # If the reversed word is in the set, it's a valid pair
            seen.add(word)  # Add the current word to the set for future checks
        return count
