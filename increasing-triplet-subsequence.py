class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        what if we try to store the minimum sofar and
        the maximum so far as we go backwards
        then check if a smaller number before and larger number after that number
        exists
        """
        #min sofar
        n = len(nums)
        min_sofar = [0]*n
        minn = float('inf')
        for idx in range(n):
            if nums[idx] < minn:
                minn = nums[idx]
            min_sofar[idx] = minn
        # max sofar
        max_sofar = [0]*n
        maxx = float('-inf')
        for idx in range(n-1, -1, -1):
            if nums[idx] > maxx:
                maxx = nums[idx] 
            max_sofar[idx] = maxx
        
        # check if such number exists
        for i in range(n):
            if min_sofar[i] < nums[i] < max_sofar[i]:
                return True
        return False