# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        i will have three pointers: prevv, curr, curr.next(nxt)
        initialization: prev = none, curr = head
        while loop: goes as long as curr and curr.next are similar
        we count how many times the loop runned
        if it runned at least once then
            nxt = curr.next
            update: prev.next = curr.next
            curr = nxt
        else:
            nxt = curr.next
            update: prev.next = curr
            curr = nxt
        
        """
        prev, curr = ListNode() , head
        dummy = prev
        while curr:
            nxt = curr.next
            count = 0
            while nxt and curr.val == nxt.val:
                curr = curr.next
                nxt = curr.next
                count += 1
            if count > 0 and nxt and nxt.next and nxt.val == nxt.next.val:
                curr = nxt
                nxt = nxt.next
                continue
            if count > 0:
                prev.next = nxt
                curr = nxt
            else:
                prev.next = curr
                prev = curr
                curr = nxt

        return dummy.next
        
                
                
                
                
                
                
