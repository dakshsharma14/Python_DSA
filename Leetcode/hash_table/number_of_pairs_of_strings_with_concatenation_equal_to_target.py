"""
what i did
"""
from typing import List


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i != j:
                    if (nums[i] + nums[j]) == target:
                        count += 1
                    if (nums[j] + nums[i]) == target:
                        count += 1
        return count
"""
using one loop from collections import Counter
from typing import List

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = 0
        freq = Counter(nums)

        # Iterate through each number in nums and check for valid pairs
        for i in range(len(nums)):
            prefix = nums[i]
            if target.startswith(prefix):
                suffix = target[len(prefix):]
                count += freq[suffix]
                
                # If the prefix and suffix are the same, subtract the pair (i, i)
                if suffix == prefix:
                    count -= 1

        return count


"""