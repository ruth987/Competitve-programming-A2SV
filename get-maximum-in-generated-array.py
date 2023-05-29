class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        """
        for evenss : nums[2*i] = nums[i]
        for odds : nums[2*i + 1] = nums[i] + nums[i+1]

        """
        mydict = {0:0, 1:1}
        
        def calc(n):
            if n not in mydict:
                m = n//2
                if n%2 == 0:
                    mydict[n] = calc(m)
                else:
                    mydict[n] = calc(m) + calc(m+1)
            return mydict[n]
        
        max_ = 0
        for n in range(n+1):
            max_ = max(max_, calc(n))
        return max_