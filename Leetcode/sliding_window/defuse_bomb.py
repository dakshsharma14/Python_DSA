from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)

        # Case 1: If k == 0, replace all elements with 0
        if k == 0:
            return [0] * n

        # Extend the array to simulate circular behavior
        extended_code = code * 2
        result = [0] * n

        # Case 2: k > 0 (sum of the next k numbers)
        if k > 0:
            for i in range(n):
                result[i] = sum(extended_code[i + 1:i + 1 + k])

        # Case 3: k < 0 (sum of the previous |k| numbers)
        else:
            for i in range(n):
                result[i] = sum(extended_code[i + n + k:i + n])

        return result

