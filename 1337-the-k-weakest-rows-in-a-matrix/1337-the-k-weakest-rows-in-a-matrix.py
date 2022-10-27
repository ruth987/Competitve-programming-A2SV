class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        output = []
        weak_to_strong = {}
        for idx, row in enumerate(mat):
            weak_to_strong[idx] = row
            
        weak_to_strong = sorted(weak_to_strong.items(), key = lambda item : (sum(item[1]), item[0]))
        
        for i in range(k):
            output.append(weak_to_strong[i][0])
        return output
            
            
            
            