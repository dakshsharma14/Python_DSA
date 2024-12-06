# class Solution:
#     def restoreString(self, s: str, indices: List[int]) -> str:
#         new_list = []
#         for i in range(len(indices)):
#             print(s[indices[i]])
#             new_list.append(s[indices[i]])
#         return "".join(new_list)
from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new_list = [''] * len(s)
        for i, index in enumerate(indices):
            new_list[index] = s[i]
        return "".join(new_list)