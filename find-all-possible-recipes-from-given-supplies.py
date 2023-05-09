class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        incomming = defaultdict(int)
        qu = deque()
        for supply in supplies:
            qu.append(supply)
        
        for i in range(len(recipes)):
            for ing in ingredients[i]:
                graph[ing].append(recipes[i])
                incomming[recipes[i]] += 1
        
        res = []
        while qu:
            length = len(qu)
            for i in range(length):
                sup = qu.popleft()
                for k in graph[sup]:
                    incomming[k] -= 1
                    if incomming[k] == 0:
                        qu.append(k)
                        res.append(k)
        return res