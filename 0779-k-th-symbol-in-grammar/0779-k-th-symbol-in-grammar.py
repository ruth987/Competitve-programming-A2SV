class Solution:
    def kthGrammar(self, row: int, k: int) -> int:
        if row == 1:
            return 0
        
        else:
            if k % 2 == 0:
                # even index of current level is opposite of parent level's [(K+1)//2]
                return 1 - self.kthGrammar(row-1, (k+1)//2)
            else:
                # odd index of current level is the same as parent level's [(K+1)//2]
                return self.kthGrammar(row-1, (k+1)//2)
            
            