from typing import List

"""
But not very optimized
"""
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j:
                    count += 1
        return count


"""

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count_dict = Counter(nums)

        newb = 0
        for n, c in count_dict.items():
            newb += c * (c - 1) // 2  # Use integer division since you're working with whole numbers
        return newb

"""
