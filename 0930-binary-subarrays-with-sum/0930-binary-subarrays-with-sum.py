class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        arr = []
        for idx in range(len(nums)):
            if nums[idx]==1:
                arr.append(idx)
        arr = [-1]+arr+[len(nums)]        
        print(arr)
        
        if goal > len(arr):
            return 0
        
        sum_ = 0
        if goal == 0:
            for i in range(1,len(arr)):
                zeros = (arr[i] - arr[i - 1])
                sum_ += (zeros*(zeros - 1))/2
            return int(sum_)
            
        
        left, right = 1, goal
        while right < len(arr)-1:
            sum_ += ((arr[left]-arr[left-1]) * (arr[right+1]-arr[right]))
            left += 1
            right += 1
        
        return sum_
    