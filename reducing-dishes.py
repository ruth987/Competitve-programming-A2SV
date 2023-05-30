class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        presum, result = 0, 0

        for i in range(len(satisfaction)):
            presum += satisfaction[i]
            if presum < 0:
                break
            result += presum

        return result