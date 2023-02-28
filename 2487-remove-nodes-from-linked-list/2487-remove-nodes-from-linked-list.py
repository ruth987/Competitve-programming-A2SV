# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # monotonic decreasing stack
        stack = []
        
        while head:
            while stack and head.val > stack[-1]:
                stack.pop()
            stack.append(head.val)
            head = head.next
        # print(stack)
        dummy = ListNode(stack[0])
        tail = dummy
        for i in range(1,len(stack)):
            tail.next = ListNode(stack[i])
            tail = tail.next
        return dummy
            
        
        