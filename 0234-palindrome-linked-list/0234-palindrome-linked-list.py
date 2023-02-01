# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        count = 0
        while fast and fast.next: #till the fast pointer reaches the end of the list
            slow = slow.next
            fast = fast.next.next
            count += 1
        # print(count)
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        # prev is the last existing slow node
        while count > 0:
            # print(prev.val, head.val)
            if prev.val != head.val:
                return False
            head = head.next
            prev = prev.next
            count -= 1
        return True
        
            
            
            
        