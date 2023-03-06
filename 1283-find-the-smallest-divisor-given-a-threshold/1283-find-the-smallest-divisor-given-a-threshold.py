class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        """
        the result we get havve to be less than or equal to threshhold
        find the smallest divisor
        divisor ranges from one to ...
        round up the dicision results. use ceil
        divisors range from 1 to max(nums)
        
        """
        left, right = 1, max(nums)
        ans = float("inf")
        while left <= right:
            mid = (left+right) //2
            cur_sum = sum(ceil(num/mid) for num in nums) 
            # print(mid, cur_sum)
            if cur_sum <= threshold:
                ans = min(ans, mid)
                right = mid-1
            elif cur_sum > threshold:
                left = mid+1

        return ans
            