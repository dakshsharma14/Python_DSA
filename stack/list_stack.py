# in this we will see the implementation of stack via list

class Stack:
    def __init__(self):
        self.stack_list = []

    # in here we use the second -1 is to he loop continues until the index reaches -1, but since the loop ends just
    # before reaching -1, it effectively stops at 0.
    # The third -1 loop iterates in reverse order, decreasing the index by 1 each time.
    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    # peek is the top most element
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()


my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print("Stack before pop():")
my_stack.print_stack()

print("\nPopped node:")
print(my_stack.pop())

print("\nStack after pop():")
my_stack.print_stack()

"""
    EXPECTED OUTPUT:
    ----------------
    Stack before pop():
    3
    2
    1

    Popped node:
    3

    Stack after pop():
    2
    1

"""