"""
This is what i thought at first
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        change_folder = []
        for i in range(len(logs)):
            if logs[i] == "../":
                if change_folder:
                    change_folder.pop()
            elif logs[i] == "./":
                continue
            else:
                change_folder.append(logs[i])
        return len(change_folder)

time complexity =
lopp O(n)
pop() is an O(1) operation.
ppend() is also O(1).

space complexity =
In the worst case,every entry in logs is appended to change_folderO(n).
Variables like i and logs[i] require constant space O(1).
"""
from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        change_folder = 0
        for i in range(len(logs)):
            if logs[i] == "../":
                if change_folder:
                    change_folder -=1
            elif logs[i] == "./":
                pass
            else:
                change_folder +=1
        return change_folder

