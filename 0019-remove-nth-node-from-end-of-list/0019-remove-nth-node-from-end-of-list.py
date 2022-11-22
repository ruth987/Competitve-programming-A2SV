# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        #shifting the right pointer to the position where we initialize
        while n>0 and right:
            right = right.next
            n-=1
            
        #trying to get the left pointer in the tobe deleted node
        while right:
            right = right.next
            left = left.next
        
        #delete
        left.next = left.next.next
        return dummy.next