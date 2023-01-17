class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # sorted and unsorted part
        for idx in range(1, len(heights)):
            if heights[idx] > heights[idx-1]:
                val = heights[idx]
                index = idx
                for i in range(idx-1,-1,-1):
                    if val>heights[i]:
                        heights[i],heights[index] = heights[index],heights[i]
                        names[i],names[index] = names[index],names[i]
                        index -= 1
        
        return names
                        