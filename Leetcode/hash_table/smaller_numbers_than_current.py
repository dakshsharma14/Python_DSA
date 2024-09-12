from typing import List
"""
memory wise good, but not runtime wise
"""

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lists = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if j != i and nums[j] < nums[i]:
                    count += 1

            lists.append(count)
        return lists

"""
better 
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)

        mapp = {}
        result = []
        for i in range(len(temp)):
            if temp[i] not in mapp:
                mapp[temp[i]] = i
        for i in range(len(nums)):
            result.append(mapp[nums[i]])
        return result

        
"""
