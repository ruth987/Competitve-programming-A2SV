# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        idx = 1
        traverse = head
        start = head
        while idx < left:
            start = traverse
            traverse = traverse.next
            idx +=1
        prev = None
        tail = traverse
        while idx >= left and idx <= right:
            nxt = traverse.next
            traverse.next = prev
            prev = traverse
            traverse = nxt
            idx +=1
        start.next = prev
        tail.next = traverse

        if left >1:
            return head
        else:
            return prev
       