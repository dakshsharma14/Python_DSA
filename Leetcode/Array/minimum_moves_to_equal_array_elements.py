from typing import List
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_value = min(nums)
        count = 0
        for num in nums:
            count += (num - min_value)
        return count
