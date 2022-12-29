class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = sorted(points, key = lambda val:(val[0]**2 + val[1]**2))
        
        return points[:k]
        
        """
        time comp: o(nlogn)
        space comp: o(1)r
        """