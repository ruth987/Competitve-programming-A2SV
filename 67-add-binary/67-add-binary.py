class Solution:
    def addBinary(self, a: str, b: str) -> str:
        while len(b)<len(a):
            b='0'+b
        while len(a)<len(b):
            a='0'+a
        carry=0
        a=[int(i) for i in a]
        b=[int(i) for i in b]
        ans=''
        for i in range(len(a)-1,-1,-1):
            val=a[i]+b[i]+carry
            if val==3:
                carry=1
                ans='1'+ans
            elif val==2:
                carry=1
                ans='0'+ans
            elif val==1:
                ans='1'+ans
                carry=0
            else:
                ans='0'+ans
        return str(carry)+ans if carry else ans