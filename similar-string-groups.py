# class DSU:
#     def __init__(self, n):
#         self.par = list(range(n))
#         self.rank = [1] * n

#     def find(self, node):
#         if self.par[node] != node:
#             self.par[node] = self.find(self.par[node])
#         return self.par[node]
    
#     def union(self, x, y):
#         px, py = self.find(x), self.find(y)
#         if self.rank[px] > self.rank[py]: 
#             self.rank[px] += self.rank[py]
#             self.par[py] = px
#         else: 
#             self.rank[py] += self.rank[px]
#             self.par[px] = py

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        parent = list(range(n)) 
        rank = [1]*n
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x]) 
            return parent[x]
        
        def union(word1, word2):
            p_w1 = find(word1)
            p_w2 = find(word2)
            if rank[p_w1] > rank[p_w2]:
                rank[p_w1] += rank[p_w2]
                parent[p_w2] = p_w1
            else:
                rank[p_w2] += rank[p_w1]
                parent[p_w1] = p_w2

        # strs.sort()
        ls = len(strs)

        for i in range(ls):
            for j in range(i + 1, ls):
                if parent[i] == parent[j]:  
                    continue
                
                unmatch = 0
                for k in range(len(strs[0])):
                    if strs[i][k] != strs[j][k]:
                        unmatch += 1
                        if unmatch > 2:
                            break
                if unmatch <= 2:
                    union(i, j)
            
        for i in range(ls):
            find(i)
        
        return len(set(parent))