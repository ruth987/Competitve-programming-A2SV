class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        gap = len(names) // 2
        
        while gap > 0:
            j = gap
            while j < len(names):
                i = j - gap
                while i >= 0:
                    if heights[i+gap] < heights[i]:
                        break
                    else:
                        heights[i+gap], heights[i] = heights[i],heights[i+gap]
                        names[i+gap], names[i] = names[i], names[i+gap]
                    i-=gap
                j+=1
            
            gap = gap//2
        return names 