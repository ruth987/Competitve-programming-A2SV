class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def findS(n):
            if n==1:
                return "0"
            return findS(n-1) +"1"+ "".join(["0" if i == "1" else "1" for i in (list(findS(n-1))[::-1])])
        
        return (findS(n))[k-1]