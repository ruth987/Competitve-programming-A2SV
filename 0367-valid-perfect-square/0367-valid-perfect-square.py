class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # time comp : o(sqrt(n))
        
        n = 1
        s = 0
        while s < num:
            s = n**2
            if s == num:
                return True
            n += 1
        return False
    