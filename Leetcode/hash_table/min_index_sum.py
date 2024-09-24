from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map_list2 = {restaurant: idx for idx, restaurant in enumerate(list2)}

        min_sum = float('inf')
        result = []

        for i, restaurant in enumerate(list1):
            if restaurant in index_map_list2:
                index_sum = i + index_map_list2[restaurant]

                if index_sum < min_sum:
                    min_sum = index_sum
                    result = [restaurant]
                elif index_sum == min_sum:
                    result.append(restaurant)

        return result
"""
i did it ---slow
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        freq = {}
        for i in range(len(list1)):
            count = 0
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    freq[list1[i]] = i + j
        min_value = min(freq.values())
        result = [key for key, value in freq.items() if value == min_value]
        return result
        

        
"""