# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or head is None:
            return head

        total = 0
        cur = head
        while cur is not None:
            cur = cur.next
            total += 1
        print(f"total len: {total}")

        if k > total:
            k = k % total

        print(f"new k: {k}")

        if k == total or k == 0:
            return head

        forward = total - k

        cur = head
        for _ in range(forward):
            cur = cur.next
        new_head = cur

        while cur.next is not new_head:
            if cur.next is None:
                cur.next = head
            else:
                cur = cur.next
        cur.next = None
        return new_head