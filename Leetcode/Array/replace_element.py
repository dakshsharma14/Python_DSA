from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Loop over each element except the last one
        for i in range(len(arr) - 1):
            # Initialize a variable to store the maximum value to the right of arr[i]
            max_value = arr[i + 1]
            # Find the maximum element from i+1 to the end of the list
            for j in range(i + 1, len(arr)):
                max_value = max(max_value, arr[j])
            # Replace arr[i] with the found max_value
            arr[i] = max_value

        # The last element should be replaced by -1
        arr[-1] = -1

        return arr
"""
from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Initialize the maximum value to -1 (as per the problem statement)
        max_from_right = -1
        
        # Traverse the array from right to left
        for i in range(len(arr) - 1, -1, -1):
            # Store the current element before updating
            current = arr[i]
            # Replace the current element with the max from right
            arr[i] = max_from_right
            # Update the max_from_right for the next iteration
            max_from_right = max(max_from_right, current)
        
        return arr

"""