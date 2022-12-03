class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return sqrt(num) == num/int(num/sqrt(num))