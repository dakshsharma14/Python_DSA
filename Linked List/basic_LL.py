# we need to add a data to a datastructure very quickly, but retrieval speed is not very important
# Linked list is the best option to choose
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_linked_list = LinkedList(4)

print(my_linked_list.head.value)
print(my_linked_list.print_list())
