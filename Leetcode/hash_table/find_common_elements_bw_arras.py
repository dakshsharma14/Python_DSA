from typing import List
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Convert nums2 to a set for faster lookup
        nums2_set = set(nums2)

        # Count the number of indices in nums1 that exist in nums2
        answer1 = sum(1 for num in nums1 if num in nums2_set)

        # Convert nums1 to a set for faster lookup
        nums1_set = set(nums1)

        # Count the number of indices in nums2 that exist in nums1
        answer2 = sum(1 for num in nums2 if num in nums1_set)

        return [answer1, answer2]



