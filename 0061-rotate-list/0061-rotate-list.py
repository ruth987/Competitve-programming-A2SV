# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        trav = head
        len_ = 0
        while trav:
            trav = trav.next
            len_ += 1
            
        n = k%len_
        if not n:
            return head
        
        slow, fast = head, head
        while fast and n:
            fast = fast.next
            n -= 1
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        new_start = slow.next
        slow.next = None
        if fast:
            fast.next = head
        return new_start
        
            
            
            
        