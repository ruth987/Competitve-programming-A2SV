class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        point_to_distance = []
        for point in points:
            distance = sqrt(point[0]**2 + point[1]**2)
            point_to_distance.append((point, distance))
            
        point_to_distance = sorted(point_to_distance, key = lambda val:val[1])
        
        answer = []
        for idx in range(k):
            answer.append(point_to_distance[idx][0])
        
        return answer
            