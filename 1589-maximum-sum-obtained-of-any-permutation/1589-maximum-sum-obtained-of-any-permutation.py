class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix = [0]*(len(nums)+1)
        
        for start,end in requests:
            prefix[start] += 1
            prefix[end+1] -= 1

        mydict = {0: prefix[0]}
        
        for idx in range(1, len(prefix)):
            prefix[idx] += prefix[idx-1]
            mydict[idx] = prefix[idx]

        mydict = sorted(mydict.items(), key = lambda item: -item[1])
        nums.sort(reverse = True)
        ans = 0
        i = 0

        for key,val in mydict:
            if val == 0:
                break
            ans += (val*nums[i])
            i += 1
        
        return ans% (10**9 + 7)
        
        
        
        