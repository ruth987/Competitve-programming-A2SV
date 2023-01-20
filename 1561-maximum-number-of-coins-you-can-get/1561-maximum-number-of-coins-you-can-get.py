class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        n = len(piles)/3 # the number of piles i will take. 
        pocket, x = 0, 0

        for idx in range(len(piles)):
            if idx%2 != 0:
                pocket += piles[idx]
                x += 1
            if x==n:
                return pocket