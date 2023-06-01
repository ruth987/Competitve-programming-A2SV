class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        for every number : the next number can be anyone of the numbers
        """
        dp = [0]*(target+1)
        dp[0] = 1

        for i in range(1, target+1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i-num]
        # print(dp)
        return dp[target]

        # def dfs(num, sum_):
        #     if sum_ == target:
        #         count += 1
        #         return
        #     for num in nums:
        #         dfs(num, sum_ + num)
        #     return
        
        # dfs()