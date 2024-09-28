# class Solution:
#     def sortSentence(self, s: str) -> str:
#         words = s.split()
#         sorted_words = [""] * len(words)
#
#         for word in words:
#             index = int(word[-1]) - 1  # Extract the index from the last character
#             sorted_words[index] = word[:-1]  # Remove the number and place the word in the correct position
#
#         return " ".join(sorted_words)


class Solution:
    def sortSentence(self, s: str) -> str:
        new = s.split()
        list_1 = [0] * len(new)
        for i in range(len(new)):
            num = int(new[i][-1]) - 1
            list_1[num] = new[i][:-1]
        return " ".join(list_1)




