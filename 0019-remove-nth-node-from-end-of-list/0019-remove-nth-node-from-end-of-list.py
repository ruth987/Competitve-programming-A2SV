# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        first find the length of the list
        then len - (k)

        """
        
        trav = head
        len_ = 0
        if n == 1:
            prev = None
            while trav.next:
                prev = trav
                trav = trav.next
            if prev:
                prev.next = None
                return head
            else:
                return prev
            
        while trav:
            trav = trav.next
            len_ += 1
            
        end_point = len_ - n
        if end_point == 0:
            return head.next
        #print(end_point)
        idx = 1
        curr = head
        prev = None
        while idx < end_point:
            curr = curr.next
            idx += 1
        curr.next = curr.next.next    
        return head
        
        
    