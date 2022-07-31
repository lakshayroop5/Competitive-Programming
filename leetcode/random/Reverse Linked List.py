# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
stack = deque
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node != null:
            stack.append(node.val)
            node = node.next
        node = head
        while len(stack) != 0:
            node.val = stack.pop()
            node = node.next
