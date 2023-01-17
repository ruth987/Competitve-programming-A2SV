class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
#         for idx in range(len(names)-1, -1, -1):
#             min_val = 10**6
#             index = 0
#             for i in range(len(heights)):
#                 if heights[i]<min_val:
#                     index = i
#                     min_val = heights[i]
#             heights[idx], heights[index] = heights[index] ,heights[idx]
#             names[idx], names[index] = names[index] ,names[idx]
        
#         return names

        for idx in range(len(names)):
            index =idx
            for i in range(idx,len(names)):
                if heights[i] > heights[index]:
                    index = i
            heights[index], heights[idx] = heights[idx], heights[index]
            names[index], names[idx] = names[idx], names[index]
        return names