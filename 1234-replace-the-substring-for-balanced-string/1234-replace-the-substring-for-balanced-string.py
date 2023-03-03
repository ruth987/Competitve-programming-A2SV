class Solution:
    def balancedString(self, s: str) -> int:

        n = len(s)
        mydict = {"Q":0 ,"W":0 ,"E":0 ,"R":0 }
        for ch in s:
            mydict[ch]+=1
        print(mydict)
        print(n)
        goal = {}
        minlen = float(inf)
        for key,val in mydict.items():
            if val > (n/4):
                goal[key] = int(val-(n/4))
        if not goal:
            return 0
        
        check = {"Q":0 ,"W":0 ,"E":0 ,"R":0 }
        left = 0
        for right in range(n):
            check[s[right]]+=1
            found = True
            for key,val in goal.items():
                if goal[key]>check[key]:
                    found = False
                    break
            # print(check, goal, found)     
            # print(s[left:right+1])
            while found and left <= right:
                
                minlen = min(minlen, right-left+1)
                check[s[left]]-=1
                left += 1
                found = True
                for key,val in goal.items():
                    if goal[key]>check[key]:
                        found = False
                        break
                # print(s[left:right+1], found)
    
        
        return minlen
                
            
            
            
        