class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        sms = 0
        sum_diff = []
        
        for index in range(len(nums)-1): #0, 1, 2
            sms += nums[index]
            left, right = index+1, len(nums)-1
            
            while left < right:
                add = nums[left]+nums[right]
                sms += add
                sum_diff.append((sms, target-sms))

                if sms > target:
                    right-=1
                elif sms < target:
                    left+=1
                else:
                    left+=1
                sms -= add
            sms -= nums[index]
        
        sum_diff = sorted(sum_diff, key = lambda item:-item[1] if item[1]<0 else item[1])
        return sum_diff[0][0]
                    
                
            
            
            
            
            
            
            
            
            
            
            
            