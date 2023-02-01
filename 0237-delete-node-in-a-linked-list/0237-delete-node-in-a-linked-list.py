# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        nextnodeval = node.next.val
        node.val = nextnodeval
        node.next = node.next.next
        