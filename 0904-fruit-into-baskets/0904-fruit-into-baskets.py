class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, right = 0, 0
        mydict, max_len = {}, 0
                
        for right in range(len(fruits)):
            if fruits[right] in mydict:
                mydict[fruits[right]]+=1
            else:
                if len(mydict)<2:
                    mydict[fruits[right]] = 1
                else: # if len(mydict)==2
                    max_len = max(max_len, right-left)
                    mydict[fruits[right]] = 1
                    while left<right:
                        mydict[fruits[left]]-=1
                        if mydict[fruits[left]]==0:
                            del mydict[fruits[left]]
                            left+=1
                            break
                        left+=1
        max_len = max(max_len, right-left+1)
        return max_len
                    
                    
                    
                    
                    
                
            
        
                
