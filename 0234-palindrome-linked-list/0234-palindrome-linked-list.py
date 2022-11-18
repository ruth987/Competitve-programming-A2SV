# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        #to get to the middle (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        #reverse from slow to the end
        prev = None
        
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        #compair the two (head and prev) linked lists
        left, right = head, prev
        
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True