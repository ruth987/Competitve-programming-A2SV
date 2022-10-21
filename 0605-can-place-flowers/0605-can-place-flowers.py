class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        possible = 0
        stack = []
        if len(flowerbed)==1 and flowerbed[0]==0:
            return 1>=n
        
        for index in range(len(flowerbed)):
            if flowerbed[index]==1:
                stack.append(flowerbed[index])
            else: # if flowerbed[index] == 0
                if not stack and flowerbed[index+1]==0:
                    possible += 1
                    stack.append(1)
                elif stack and stack[-1]==1:
                    stack.append(flowerbed[index])
                elif stack and stack[-1]==0 and index == len(flowerbed)-1:
                    possible += 1
                    stack.append(1)
                elif stack and stack[-1]==0 and flowerbed[index+1]==0:
                    possible += 1
                    stack.append(1)
                    
        return possible >= n
                