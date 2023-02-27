class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix = [0]*(len(nums)+1)
        
        for start,end in requests:
            prefix[start] += 1
            prefix[end+1] -= 1

        for idx in range(1, len(prefix)):
            prefix[idx] += prefix[idx-1]

        prefix.sort(reverse = True)
        nums.sort(reverse = True)
        ans = 0
        i = 0

        for i in range(len(nums)):
            if prefix[i]==0:
                break
            ans += (prefix[i]*nums[i])
        
        return ans% (10**9 + 7)
        
        
        
        