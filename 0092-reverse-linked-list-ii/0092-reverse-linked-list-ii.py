# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cp,tv,lenn,vals = head,head,0,[]
        while tv:
            vals.append(tv)
            lenn,tv=lenn+1,tv.next
        #print(vals)
        left,right = left-1,right-1
        while left < right:
            vals[left].val,vals[right].val = vals[right].val,vals[left].val
            left,right = left+1,right-1
        return cp