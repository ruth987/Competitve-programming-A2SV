class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        start, end = 0, len(skill)-1
        sum_ = skill[0]+skill[-1]
        chemistry = 0
        
        while start < end:
            if skill[start]+skill[end] != sum_:
                return -1
            chemistry += (skill[start]*skill[end])
            start += 1
            end -= 1
        return chemistry
    