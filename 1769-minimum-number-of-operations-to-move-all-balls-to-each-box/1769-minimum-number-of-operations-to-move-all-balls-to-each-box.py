class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ones_index = []
        
        for idx in range(len(boxes)):
            if  boxes[idx]=="1":
                ones_index.append(idx)

        answer = [0]*len(boxes)
        for idx in range(len(boxes)):
            for i in ones_index:
                if i != idx:
                    answer[idx] += abs(i-idx)
                    
        return answer
                
