class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        do it with top down approach

        change each member of the array into max money that can be robbed upto that
        house
        """ 
        # if len(nums)==1: return nums[0]

        # maxrob = [0]*len(nums)
        # maxrob[0], maxrob[1] = nums[0], max(nums[0], nums[1])
        # for idx in range(2, len(nums)):
        #     maxrob[idx] = max(maxrob[idx-1], nums[idx] + maxrob[idx-2])
        
        # return maxrob[len(nums)-1]

        @cache
        def maxrob(idx):
            if idx == 0 or idx == 1:
                return max(nums[:idx+1])
            
            return max(maxrob(idx-1), nums[idx] + maxrob(idx-2))

        return maxrob(len(nums)-1)