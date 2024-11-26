from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        for i in logs:
            if i=="./":
                continue
            elif stack and i=="../":
                stack.pop()
            elif i!='../':
                stack.append(i)
        return len(stack)
#space complexity: as we are acreating the stack then we can say it can have O(n) in worst case
#time complexity O(n) and Checking conditions = o(1)