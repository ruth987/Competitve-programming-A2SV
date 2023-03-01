class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x, n):
            if n == 0:
                return 1
            elif n < 0:
                n = abs(n)
                if n==1:
                    return 1/x

                if n%2 == 0:
                    var = (1/pow(x, n//2))
                    return var* var
                else: # for odd
                    var = (1/pow(x, n//2)) 
                    return var* var* (1/x)
            else:
                if n==1:
                    return x

                if n%2 == 0:
                    var = pow(x, n//2)
                    return  var* var
                else: # for odd
                    var =  pow(x, n//2)
                    return var * var*x

        return pow(x, n)
            