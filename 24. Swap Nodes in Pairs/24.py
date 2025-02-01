# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        dummy2 = None
        first, odd = True, True
        while cur is not None:
            if odd and cur.next is not None:
                dummy = cur.next
                cur.next = dummy.next
                dummy.next = cur

                if dummy2 is not None:
                    dummy2.next = dummy
                
                if first:
                    head = dummy
                    first = False
                
            dummy2 = cur
            cur = cur.next
            
        return head