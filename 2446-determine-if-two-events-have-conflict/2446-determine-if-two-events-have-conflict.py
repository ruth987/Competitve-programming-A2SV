class Solution:
    def haveConflict(self, a: List[str], b: List[str]) -> bool:
        a_start, a_end = a
        b_start, b_end = b
        return b_start <= a_start <= b_end or \
               b_start <= a_end <= b_end or \
               a_start <= b_start <= a_end or \
               a_start <= b_end <= a_end
            