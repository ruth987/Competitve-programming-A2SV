class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        n = int(num**0.5)
        for number in range(0, n+1):
            if number*number == num:
                return True
        return False
    