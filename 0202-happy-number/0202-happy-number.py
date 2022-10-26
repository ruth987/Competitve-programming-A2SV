class Solution:
    def isHappy(self, n: int) -> bool:
        aset = set()
        def sumofsquares(n):
            output = 0
            for digit in range(len(str(n))):
                output += ((int((str(n))[digit]))**2)
            return output
                
        while n not in aset:
            aset.add(n)
            n = sumofsquares(n)
            if n==1:
                return True
        return False
            
            