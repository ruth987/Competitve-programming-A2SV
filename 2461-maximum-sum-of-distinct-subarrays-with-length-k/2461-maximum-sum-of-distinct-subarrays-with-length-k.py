class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        seen = set()
        right,left,ans,sub_sum = 0,0,0,0

        while right < len(nums): 
            if len(seen) != k:
                if nums[right] not in seen: 
                    seen.add(nums[right])
                    sub_sum += nums[right]
                    right+=1 
                else: 
                    seen.remove(nums[left])
                    sub_sum -= nums[left]
                    left += 1 
            else: 
                ans = ans if ans > sub_sum else sub_sum
                seen.remove(nums[left])
                sub_sum -= nums[left]
                left += 1


        if len(seen) == k: 
            ans = ans if ans > sub_sum else sub_sum
        return ans 
        """
        left, right = 0, k-1
        seen = set()
        sub_sum = 0
        
        for idx in range(k-1):
            seen.add(nums[idx])
            sub_sum += nums[idx]
        max_sum = 0
        
        while right < len(nums):
            sub_sum += nums[right]
            seen.add(nums[right])
            
            if len(seen)==k:
                max_sum = max(max_sum, sub_sum)
            
            left+=1
            right+=1
            seen.remove(nums[left-1])
            sub_sum -= nums[left-1]
        return max_sum
        
        """
        
    """
    class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        seen = set()
        sm = 0 
        ans = 0
        right = 0 
        left = 0 
        while right < len(nums): 
            if len(s) != k:
                if nums[right] not in seen: 
                    seen.add(nums[right])
                    sm += nums[right]
                    right+=1 
                else: 
                    seen.remove(nums[left])
                    sm -= nums[left]
                    left += 1 
            else: 
                ans = ans if ans > sm else sm
                s.remove(nums[left])
                sm -= nums[left]
                left += 1


        if len(seen) == k: 
            ans = ans if ans > sm else sm
        return ans 
    
    """