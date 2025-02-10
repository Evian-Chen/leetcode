# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        if cur is None:
            return head
        else:
            ans = ListNode(0)
            d = ans
            du = False
            while cur.next is not None:
                if cur.next.val != cur.val:
                    if not du:
                        d.next = cur
                        d = d.next
                    else:
                        du = False
                    cur = cur.next
                else:
                    du = True
                    cur = cur.next
            d.next = None if du else cur
            return ans.next
