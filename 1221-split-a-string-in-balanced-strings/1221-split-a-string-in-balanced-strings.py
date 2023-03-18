class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count,amount=0,0
        for i in s:
            if i == "R":
                count+=1
            else:
                count-=1
            if count==0:
                amount+=1
        return amount
    
    
    
    
    
    
    