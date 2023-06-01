class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        """
        we have two cases :
            if we take first element 
            else if we dont take the first element
        
        num + diff = sth in mydict
        
        """
        mydict = Counter()
        for num in arr:
            mydict[num] = max(mydict[num], 1 + mydict[num-difference])

        return max(mydict.values())