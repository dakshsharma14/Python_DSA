from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()  # Set to store elements in the current window
        for i in range(len(nums)):
            # Check if the current element is already in the window
            if nums[i] in window:
                return True
            # Add the current element to the window
            window.add(nums[i])
            # If the window size exceeds k, remove the leftmost element
            if len(window) > k:
                window.remove(nums[i - k])

        return False

