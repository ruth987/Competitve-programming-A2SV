# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        curr = head
        next_el = curr.next
        while curr and next_el:
            # print(next_el.val , curr.val)
            if next_el.val !=  curr.val:
                curr.next = next_el
                curr = next_el
            if next_el.val ==  curr.val and not next_el.next:
                curr.next = next_el.next
            next_el = next_el.next
        return head
                