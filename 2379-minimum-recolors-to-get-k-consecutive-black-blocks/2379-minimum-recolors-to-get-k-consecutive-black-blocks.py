class Solution:
	def minimumRecolors(self, blocks: str, k: int) -> int:
        
            left, right = 0, 0
            operation = 0
            op = []
            while right < len(blocks):  
                if blocks[right] == "W":
                    operation+=1
                if right == left+k-1:
                    op.append(operation)
                    while blocks[left]!= "W" and left<right:
                        left+=1
                    left+=1
                    if operation >0:
                        operation-=1 
                right+=1
            return min(op)
        
                
            
