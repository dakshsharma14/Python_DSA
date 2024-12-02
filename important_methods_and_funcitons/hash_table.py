'''
Can be use to track the occurence of the values
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for item in nums:
            if item in my_dict:
                return True
            else:
                my_dict[item] = 1
        return False
'''