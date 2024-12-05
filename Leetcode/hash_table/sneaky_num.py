from _ast import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # maps = {}
        # new=[]
        # for i in range(len(nums)):
        #     if nums[i] in maps:
        #         new.append(nums[i])
        #     else:
        #         maps[nums[i]]= 1
        # return new
        seen = set()  # Use a set to track seen numbers
        new = []  # List to store sneaky numbers
        for num in nums:
            if num in seen:  # Check if the number is already in the set
                new.append(num)
            else:
                seen.add(num)  # Add the number to the set
        return new