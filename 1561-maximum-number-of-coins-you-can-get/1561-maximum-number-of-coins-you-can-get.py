class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        piles = piles[::-1]
        n = len(piles)//3
        ans = []
        idx = 1
        i = 0
        while i<n:
            ans.append(piles[idx])
            i+=1
            idx += 2
        print(ans)
        return sum(ans)
    