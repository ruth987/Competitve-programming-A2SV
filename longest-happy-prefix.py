class Solution:
    def longestPrefix(self, s: str) -> str:
        def lps(s):
            LPS = [0]*len(s)
            previdx, idx = 0, 1

            while idx < len(s):
                if s[previdx] == s[idx]:
                    # print(previdx, idx, LPS)
                    LPS[idx] = previdx + 1
                    previdx += 1
                    idx += 1
                    
                else:
                    if previdx == 0:
                        idx += 1
                    else:
                        previdx = LPS[previdx-1]
            return LPS
        
        arr = (lps(s))

        return s[len(s) - arr[-1] : ]