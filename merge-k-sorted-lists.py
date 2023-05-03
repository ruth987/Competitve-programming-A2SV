# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        (node.val, node)
        (1, 0, node)
        (1, 1,node)
        (2, node)
        n log(k)
        n log(n)
        so how can we implement it?
        """
        # ended = set()
        dummy = ListNode(0)
        newhead = dummy
        my_heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(my_heap,(lists[i].val, i, lists[i]))
        
        while my_heap:
            smallest = heapq.heappop(my_heap)
            dummy.next = smallest[2]
            dummy = dummy.next
            if smallest[2].next:
                heapq.heappush(my_heap, (smallest[2].next.val, smallest[1],smallest[2].next))

        return newhead.next