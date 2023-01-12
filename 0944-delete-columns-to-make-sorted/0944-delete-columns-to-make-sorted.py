class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        """
        n strings --> have same length
        
        
        """
        count = 0
        n = len(strs[0])
        the_strings = []
        
        for idx in range(n):
            poss = ""
            for word in strs:
                poss+= word[idx]
            the_strings.append(poss)
        
        for word in the_strings:
            if word!= "".join(sorted(word)):
                count += 1
        
        return count 
            
            