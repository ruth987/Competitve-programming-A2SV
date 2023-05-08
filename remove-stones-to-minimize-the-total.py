class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        """
        return : minimum possible total number of stones after k operations

        piles = [5,4,9], k = 2
                [5,4,5], k = 1
                [3,4,5], k = 0 ans : 10 
        ==> so basically choose the biggest number, pop it, divide it then round 
        up the number then push it back to the heap    
        """
        piles = [-pile for pile in piles]
        heapq.heapify(piles)
        while k > 0:
            num = -heapq.heappop(piles)
            heapq.heappush(piles, -ceil(num/2))
            k -= 1
        
        return abs(sum(piles))