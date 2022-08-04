class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        i = head
        j = i.next
        k = j.next

        # while i == head
        i.next = None
        j.next = None
        i.next = k
        j.next = i
        head = j
        p = i

        # for the rest of the list
        while i and j:
            p = i
            i = k
            if i is None:
                break
            j = i.next
            if j is None:
                break
            k = j.next
            p.next = None
            i.next = None
            j.next = None
            i.next = k
            j.next = i
            p.next = j
        return head
