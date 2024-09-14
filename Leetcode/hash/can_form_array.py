from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        dic = {piece[0]: piece for piece in pieces}
        res = []
        for x in arr:
            if x in dic:
                # not append
                res.extend(dic[x])
        return res == arr
