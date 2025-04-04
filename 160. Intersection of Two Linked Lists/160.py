# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA and not headB:
            return None

        ref_s = set()
        cur = headA
        while cur is not None:
            ref_s.add(cur)
            cur = cur.next

        cur = headB
        while cur is not None:
            if cur in ref_s:
                return cur
            cur = cur.next

        return None
