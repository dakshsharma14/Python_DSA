from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ops = 0
        for i in range(len(nums)):
            if ((nums[i] + 1) % 3 == 0) or ((nums[i] - 1) % 3 == 0):
                ops += 1
        if ops == 0:
            return 0
        return ops


