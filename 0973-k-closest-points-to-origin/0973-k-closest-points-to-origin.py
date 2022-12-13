class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key = lambda val: val[0]**2 + val[1]**2)
        answer=[]
        for x in range(k):
            answer.append(points[x])
        return answer
            
        