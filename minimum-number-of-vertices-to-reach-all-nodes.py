class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # so the task is basically to print out those vertices 
        # that has an outputs but dont input

        # store that has inputs
        inputers = set()
        for x,y in edges:
            inputers.add(y)
        print(inputers)
        ans = set()
        for x,y in edges:
            if x not in inputers:
                ans.add(x)
        if not ans:
            return [edges[0][1]]
        else:
            return list(ans)