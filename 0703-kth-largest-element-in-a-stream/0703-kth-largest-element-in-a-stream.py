class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        """
        kth largest element- so we count from the end of the array and return the
        kth value from the end if it is sorted in ascending order.
        
        original - [2,4,5,8]
        insert 3 - [2,3,4,5,8]
        insert 5 - [2,3,4,5,5,8]
        insert 10 -[2,3,4,5,5,8,10]
        insert 9 - [2,3,4,5,5,8,9,10]
        insert 4 - [2,3,4,4,5,5,8,9,10]
        
        
        """
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)