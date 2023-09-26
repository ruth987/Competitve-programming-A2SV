class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        """
        for every time: i have two choice
            - to take that satisfaction
            - to not take that satisfaction
        two states : idx, count
        """
        satisfaction.sort()
        n = len(satisfaction)
        @cache
        def dp(idx, count):
            print("idx", idx, count)
            
            if idx >= n:
                return 0
            ch1 = dp(idx+1, count+1) + (satisfaction[idx]*count)
            ch2 = dp(idx+1, count)
            # print(ch1, ch2)
            return max(ch1, ch2)
            
        return dp(0, 1)