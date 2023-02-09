# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        k_beg = None
        k_end = None
        
        slow, fast = head, head
        count = 0
        while fast and count < k-1:
            fast = fast.next
            count += 1
        k_beg = fast
        while fast.next:
            slow = slow.next
            fast = fast.next
        k_end = slow
        #print(k_beg, k_end)
        temp = k_beg.val
        k_beg.val = k_end.val
        k_end.val = temp
        
        return head
            
            