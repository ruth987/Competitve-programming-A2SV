from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        length = len(s1)
        for i in range(len(s2)):
            if s2[i] in s1_counter:
                s1_counter[s2[i]] -= 1
            if i >= length and s2[i - length] in s1_counter:
                s1_counter[s2[i - length]] += 1
            if all([s1_counter[i] == 0 for i in s1_counter]): 
                return True
        return False