class Solution:
    def tribonacci(self, n: int) -> int:
        """
        0 1 1 2 4 7 13 

        each number is the sum of the last three numbers

        """
        mydict = {0:0, 1:1, 2:1}
        def tribo(n):
            if n not in mydict:
                mydict[n] = tribo(n-1)+tribo(n-2)+tribo(n-3)
            return mydict[n]
        
        return tribo(n)