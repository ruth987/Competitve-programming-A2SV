class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        ln = len(citations)
        left, right = 0, ln-1
        ans = 0
        
        while left <= right:
            mid = (left+right)//2
            
            if citations[mid] == ln - mid:
                return citations[mid]
            elif citations[mid] > ln - mid:
                right = mid - 1
            else:
                left = mid + 1
        return ln - left
        
        