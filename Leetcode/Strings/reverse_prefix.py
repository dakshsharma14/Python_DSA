# class Solution:
#     def reversePrefix(self, word: str, ch: str) -> str:

#         point = 0
#         for i in range(len(word)):
#             if ch == word[i]:
#                 point = i
#                 break
#         string = ""
#         for i in range(point+1):
#             string = string + word[i]
#         string = string[::-1]
#         for j in range(point+1, len(word)):
#             string += word[j]
#         return string
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # Find the first occurrence of 'ch'
        point = word.find(ch)

        # If 'ch' is found, reverse the prefix, otherwise return the original word
        if point != -1:
            return word[:point + 1][::-1] + word[point + 1:]
        else:
            return word


