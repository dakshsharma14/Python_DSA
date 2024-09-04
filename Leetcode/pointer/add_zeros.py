"""
this is what i did, but takes up the memory but is not valid for this question
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        l1 = []
        l2 = []
        for i in range(len(nums)):
            if nums[i] == 0:
                l2.append(nums[i])
            elif nums[i] != 0:
                l1.append(nums[i])
        l3 = l1 + l2
        for i in range(len(nums)):
            nums[i] = l3[i]


            below code is using two pointer approach
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l +=1
        return nums



