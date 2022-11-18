# Definition for singly-linked list.
# class ListNode:
#     def _val_init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''the concept of two pointers in linked list-->the fast and slow pointers'''
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        this is basically the same as returning the value or the point ar which the 
        slow pointer is pointing at and actually not the value we are supposed to return 
        the node so basically we are return the list that starts from the middle and ends
        at the end of the given list
        """
        slow, fast = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        return slow