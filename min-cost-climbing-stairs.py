class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        last1, last2 = cost[-1], 0

        for idx in range(len(cost)-2,-1,-1):
            temp = last1
            last1  = min(last1, last2)+cost[idx]
            last2 = temp
        return min(last1, last2)