# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1, head2 = list1, list2
        dummy = ListNode()
        ans = dummy
        while head1 and head2:
            if head1.val < head2.val:
                dummy.next = head1
                head1 = head1.next
            else: # head2.val < head1.val
                dummy.next = head2
                head2 = head2.next
            dummy = dummy.next
        if not head1:
            dummy.next = head2
        elif not head2:
            dummy.next = head1
            
        return ans.next
        