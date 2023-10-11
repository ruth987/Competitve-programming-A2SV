# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         l, r = 0, len(needle)-1

#         l_n = len(needle)-1
#         n = l_n
#         startval = 0
#         for lt in needle:
#             startval += ((26**n )* (ord(lt)-96))
#             n -= 1
#         print("startval", startval)

#         print(ord('l')-96)
#         l, r = 0, 0
#         n = l_n
#         val = 0
#         while r < len(haystack):
#             if r < len(needle):
#                 val += ((26**n) * (ord(haystack[r])-96))

#             if val == startval:
#                 return l
#             # r_pos = (r+1) % len(needle) 
#             if n == 0:
#                 print("r", r, haystack[l:r+1], val)
#                 val -= ((26**l_n)*(ord(haystack[l])-96))
#                 val *= 26 
#                 val += ((ord(haystack[r]) - 96))
#                 print("af", val)
#                 l += 1
#                 n = l_n
#             n -= 1
#             r += 1
        
#         return -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
            
        if not needle:
            return 0 
 
        l_n = len(needle)
        startval = 0
        val = 0

        for i in range(min(len(haystack), l_n)):
            startval = startval * 26 + (ord(needle[i]) - ord('a'))
            val = val * 26 + (ord(haystack[i]) - ord('a')) 

        if startval == val:
            return 0  

        for r in range(l_n, len(haystack)):
            val = val * 26 + (ord(haystack[r]) - ord('a'))
            val -= (ord(haystack[r - l_n]) - ord('a')) * (26 ** l_n)

            if val == startval:
                return r - l_n + 1

        return -1