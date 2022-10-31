class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        mylist, answer = [], []
        
        
        for idx in range(len(l)):
            mylist = nums[l[idx]:r[idx]+1]
            mylist.sort()
            diff, x = mylist[1]-mylist[0], 0
            
            for index in range(2,len(mylist)):
                if (mylist[index]-mylist[index-1]) != diff:
                    answer.append(False)
                    x = 1
                    break
            if x == 0:
                answer.append(True)
        return answer
                    
                
                
            
            
            
            
            
        