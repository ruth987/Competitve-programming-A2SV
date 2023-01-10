class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = [0]*len(boxes)
        
        for idx in range(len(boxes)):
            for i in range(len(boxes)):
                if i != idx and boxes[i]=="1":
                    answer[idx] += abs(i-idx)
        return answer