class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # find the last friend in the circle.
        """
        n = 5, k = 2
        [1,2,3,4,5]
        """
        alist = [i for i in range(1,n+1)] #[1,2,3,4,5]
        idx = 0
        count = 0
        while len(alist)>1: 
            index = idx%len(alist)
            count += 1
            
            if count == k:
                print(alist[index])
                alist.pop(index)
                count = 0
                idx -= 1
            if idx == len(alist)-1:
                idx  = 0
                continue
            idx += 1
        return alist[0]
            