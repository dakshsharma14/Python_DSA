from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        # for i in range(len(words)):
        #     start, end = 0, len(words[i]) - 1
        #     while start < end:
        #         if words[i][start] != words[i][end]:
        #             break
        #         start += 1
        #         end -= 1
        #     else:
        #         return words[i]
        # return ""

        for word in words:
            if word == word[::-1]:
                return word
        return ""
