class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.p = {i:i for i in range(len(accounts))} 
               
        em_ac = dict() 
        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in em_ac:
                    self.union(em_ac[email], i)
                    continue
                
                em_ac[email] = i
    
        ac_em = dict() 
        for email in em_ac:
            acc = self.find(em_ac[email])
            
            if acc in ac_em:
                ac_em[acc].append(email)
            else:
                ac_em[acc] = [email]
             
        res = []   
        for p in ac_em:
            res.append([accounts[p][0]] + sorted(ac_em[p]))
            
        return res
    
    def union(self, a, b):
        self.p[self.find(b)] = self.find(a)

    def find(self, res):
        while self.p[res] != res:
            self.p[res] = self.p[self.p[res]]
            res = self.p[res]

        return res