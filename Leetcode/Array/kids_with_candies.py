from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candie = max(candies)
        result = []
        for candy in candies:
                result.append(candy+extraCandies >= max_candie)
        return result