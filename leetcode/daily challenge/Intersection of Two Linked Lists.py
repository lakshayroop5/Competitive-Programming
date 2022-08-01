class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        seen = dict()
        cur = headA
        while cur:
            seen[cur] = 1
            cur = cur.next

        cur = headB
        while cur:
            if cur in seen:
                return cur
            cur = cur.next

        return None
