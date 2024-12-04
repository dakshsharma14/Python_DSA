"""
very slow
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_list = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    new_list.append(i)
                    new_list.append(j)
        return new_list



"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}  # stores the value and its index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[num] = i
        return []
