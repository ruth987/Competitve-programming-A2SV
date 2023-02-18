# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s=set()
        curr=head
        while curr:
            if curr in s:
                return curr
            s.add(curr)    
            curr=curr.next
         