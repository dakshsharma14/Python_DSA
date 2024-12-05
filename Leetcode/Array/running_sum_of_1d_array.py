from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        count = 0
        new = []
        for i in range(len(nums)):
            count = nums[i] + count
            new.append(count)
        return new


'''
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(map(lambda x: x, accumulate(nums)))
'''