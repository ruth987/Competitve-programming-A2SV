class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        for number in range(0, int(num**0.5)+1):
            if number*number == num:
                return True
        return False