# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return head
        
        cur = head

        dum = ListNode()
        cur_d = dum

        sub_head = ListNode()
        cur_s = sub_head

        while cur.next is not None:
            if cur.val >= x:
                cur_s.next = cur
                cur_s = cur_s.next
            else:
                cur_d.next = cur
                cur_d = cur_d.next
                cur_s.next = None
            cur = cur.next

        if cur.val >= x:
            cur_s.next = cur
            cur_s = cur_s.next
        else:
            cur_d.next = cur
            cur_d = cur_d.next
            cur_s.next = None

        cur_d.next = sub_head.next

        return dum.next