class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ptr1, ptr2 = 0, 0
        count = 0
        g.sort()
        s.sort()
        while ptr1 < len(g) and ptr2 < len(s):
            if s[ptr2] >= g[ptr1]:
                count += 1
                ptr1 += 1
                ptr2 += 1
            else:
                ptr2 += 1
        
        return count