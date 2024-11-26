from typing import Optional

from Leetcode.LinkedList.has_cycle import ListNode


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# time = the loop iterates approximately n/2  time. remove the factor = O(n)
# space = o(1) No additional data structures and The function uses a fixed amount of memory for the pointers slow and fast