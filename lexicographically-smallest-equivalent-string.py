class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        """
        what if i create a union for all the letters that are equal 

        always make the letter that is lexigographically the smallest the represen
        tative of the group that way i can be sure that it is mapped with the 
        right letter and i can simply take it and construct the result
        """
        parent = {}
        def representative(x):
            if x not in parent:
                parent[x] = x
            elif x != parent[x]:
                parent[x] = representative(parent[x])
            return parent[x]
        
        def union(letter1, letter2):
            p_l1 = representative(letter1)
            p_l2 = representative(letter2)

            if p_l1 < p_l2:
                parent[p_l2] = p_l1
            else:
                parent[p_l1] = p_l2
            
        for i in range(len(s1)):
            union(s1[i], s2[i])
        
        ans = []
        for let in baseStr:
            ans.append(representative(let))

        return "".join(ans)