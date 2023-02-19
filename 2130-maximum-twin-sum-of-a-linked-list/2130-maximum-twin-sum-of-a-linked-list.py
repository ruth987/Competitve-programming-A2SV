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
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        print(arr)
        n = len(arr)//2
        back_idx = -1
        max_sum = 0
        for i in range(n):
            print(arr[i], arr[n])
            max_sum = max(max_sum, arr[i]+arr[back_idx])
            back_idx -= 1
        
        return max_sum
        
            
            
        