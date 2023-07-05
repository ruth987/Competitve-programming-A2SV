class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        """
        values[i] + i and values[j] - j
        """
        i, j = 0, 1
        max_ = values[i] + values[j] + i - j
        sofar = values[i] + i

        for idx in range(1, len(values)):
            max_ = max(max_, sofar + values[idx] - idx)
            sofar = max(sofar, values[idx]+idx)
        
        return max_