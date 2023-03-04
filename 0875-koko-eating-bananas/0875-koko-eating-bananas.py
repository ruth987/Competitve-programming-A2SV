class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        ans = right
        
        while left <= right:
            mid = (left+right)//2
            
            hr = 0
            for pile in piles:
                hr += ceil(pile/mid)
            
            if hr <= h:
                ans = min(ans, mid)
                right = mid-1
            else:
                left = mid+1
        
        return ans
    