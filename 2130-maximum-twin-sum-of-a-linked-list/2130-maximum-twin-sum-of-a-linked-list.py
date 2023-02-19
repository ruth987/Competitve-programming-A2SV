# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        """
        twin nodes : i-th node and n-1-i th node
        
        4 9 6 4 6 8 0 
        0 1 2 3 4 5 6
        brute force approach: save it in an array then access the twins through index
        """
        # find the length of the linked list
        length = 0
        traverse = head
        while traverse:
            length += 1
            traverse = traverse.next
        # print(length)
        prev = None
        curr = head
        idx = 0
        while idx < length:
            if idx == (length//2):
                prev.next = None
            if idx >= (length//2):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            else:
                prev = curr
                curr = curr.next
            idx += 1
        # print(head, prev)
        # prev is the start of the end part 
        # head is the start of the first part 
        
        max_sum = 0
        while head and prev:
            max_sum = max(max_sum, (head.val+prev.val))
            head = head.next
            prev = prev.next
        return max_sum 
        
            
        
        
            
            
        