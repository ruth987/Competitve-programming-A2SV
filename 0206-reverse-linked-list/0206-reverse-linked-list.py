# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        emp-->1-->2-->3-->4-->5-->emp
             prev cur  curr.next

        """
        previous, current = None, head
        while current: #i want the while loop to keep going as long as the curr isnot null
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt
        
        return previous
