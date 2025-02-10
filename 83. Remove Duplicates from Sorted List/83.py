# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is not None:
            front, last = head.next, head
            while front is not None:
                if front.val == last.val:
                    last.next = front.next
                    front = last.next
                else:
                    last = front
                    front = front.next
            return head
        return head