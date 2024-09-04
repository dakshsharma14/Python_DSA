"""
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        k2 = []

        # Step 1: Populate k2 with unique elements while maintaining order
        for num in nums:
            if num not in seen:
                k2.append(num)
                seen.add(num)

        # Step 2: Modify nums in place to contain the unique elements at the start
        for i in range(len(k2)):
            nums[i] = k2[i]

        # Step 3: If there are remaining positions in nums, fill them with placeholders (if needed)
        for i in range(len(k2), len(nums)):
            nums[i] = "_"

        # Step 4: Return the number of unique elements
        return len(k2)
best way is below
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l+=1
        return l