class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        """
        from big height to small height
        """
        mydict = list(zip(names, heights))
        mydict = sorted(mydict, key = lambda item:-item[1])
        ans = []
        for item in mydict:
            ans.append(item[0])
        
        return ans
