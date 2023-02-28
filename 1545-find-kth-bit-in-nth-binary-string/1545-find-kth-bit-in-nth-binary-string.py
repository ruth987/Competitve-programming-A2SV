class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def findS(n):
            if n==1:
                return "0"
            
            var = list(findS(n-1))
            new_var = var[:]
            
            for i in range(len(var)):
                if new_var[i]=="1":
                    new_var[i] = "0"
                else:
                    new_var[i] = "1"
            new_var = new_var[::-1] 
            return "".join(var) + "1"+ "".join(new_var)
        
        return (findS(n))[k-1]