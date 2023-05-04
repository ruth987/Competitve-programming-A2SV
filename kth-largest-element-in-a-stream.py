class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # initialize a heap with size k
        # [4, 5, 8, 2] - [2, 4, 5, 8] 
        new_arr = []
        x = 0
        for num in nums:
            if len(new_arr) < k:
              heapq.heappush(new_arr, num)
            else:
              if num > new_arr[0]:
                heapq.heappushpop(new_arr, num)
        
        self.nums = new_arr
        self.k = k

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
          heapq.heappush(self.nums, val)
        else:
          if val > self.nums[0]:
            heapq.heappushpop(self.nums, val)
        return self.nums[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)