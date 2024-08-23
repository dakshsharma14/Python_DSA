# path to the problem : - https://leetcode.com/problems/min-stack/description/
"""
we are taking two list
stack that will store each element
min stack will store same things but will compare the appended value with the value at the
top of the stack

"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)

        if self.min_stack:
            self.min_stack.append(min(x, self.min_stack[-1]))
        else:
            self.min_stack.append(x)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
        else:
            pass

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return -1

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return -1

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
