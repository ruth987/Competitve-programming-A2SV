class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        """
        the parent of each is either one or zero
        """
        parent = {}
        def representative(x):
            if x not in parent:
                parent[x] = x
            elif x != parent[x]:
                parent[x] = representative(parent[x])
            return parent[x]
        
        def union(l1, l2):
            p_l1 = representative(l1)
            p_l2 = representative(l2)

            if p_l1 != p_l2:
                parent[p_l1] = p_l2

        for comb in equations:
            if comb[1:3] == "==":
                union(comb[0], comb[-1])
                
        for comb in equations:
            if comb[1:3] == "!=":
                if representative(comb[0])==representative(comb[-1]):
                    return False
        return True