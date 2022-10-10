import collections

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        answer = []
        left, right = 0, len(p)
        p_dict = collections.Counter(p)

        while right < len(s)+1:
            s_dict = collections.Counter(s[left:right])
            if s_dict == p_dict:
                answer.append(left)
            left+=1
            right+=1
                
        return answer
                