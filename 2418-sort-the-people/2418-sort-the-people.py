class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        """
        from big height to small height
        """
        # mydict = dict(zip(names, heights))
        # print(mydict)
        i = 0
        while i < len(heights)-1:
            flag = False
            for idx in range(len(heights)-1):
                if heights[idx] < heights[idx+1]:
                    heights[idx], heights[idx+1] = heights[idx+1], heights[idx]
                    names[idx], names[idx+1] = names[idx+1], names[idx]
                    flag = True
            if flag == False:
                break
            i += 1
            
        return names  