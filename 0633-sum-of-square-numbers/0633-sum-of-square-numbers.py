class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        half_of_num = int(c**0.5)
        left, right = 0, half_of_num
        
        while left <= right:
            res = (left**2) + (right**2)
            if res == c:
                return True
            elif res < c:
                left += 1
            else:
                right -= 1
        return False
       