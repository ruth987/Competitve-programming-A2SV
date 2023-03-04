class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        left, right = 1, sum(weights)
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            windows = 1
            sum_ = 0
            flag = True
            for weight in weights:
                if (sum_ + weight) > mid:
                    windows += 1
                    sum_ = 0
                    if weight > mid:
                        flag = False
                        break
                sum_ += weight
                
            if windows > days or not flag:
                left = mid + 1     
            else:
                ans = mid
                right = mid - 1
                
        return ans