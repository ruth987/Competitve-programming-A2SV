class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        a function : row sum: finds the sum of the row using two pointers
        it works by requesting the row sum of the above row ...
        this goes all the way to the begining till the row number become s
        zero --> base case -- we get one from that
        
        """
        def rowsum(alist):
            left, right = 0, 1
            newlist = []
            while right < len(alist):
                newlist.append(alist[left]+alist[right])
                left += 1
                right += 1
            return newlist
       
        def pascal(rowindex):
            if rowindex==0:
                return [1]
            if rowindex==1:
                return [1,1]
    
            return [1]+rowsum(pascal(rowindex-1))+[1]
        
        return pascal(rowIndex) 
                
        
