class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
        safe node: every path that starts from it leads to terminal(safe) node
        we can use colors to differenciate between safe and unsafe nodes
        color = 1(unsafe means there is a cycle that includes this node)
        color = 2(safe everything from here leads to another safe node)
        color = 0(we haven't visited it yet)

        do dfs for all nodes:
        if we encounter
            1, safe node -> do dfs for all paths
            2, unsafe node -> the dfs path is unsafe
            3, 2 -> all the path afterward is safe
        add all safe nodes(==2) to the result then return that

        """
        color = [0 for _ in range(len(graph))]

        def dfs(index):
            if color[index] == 1:
                return False
            if color[index] == 2:
                return True

            color[index] = 1
            for nei in graph[index]:
                if color[nei] == 1 or not dfs(nei):
                    color[index] = 1
                    return False

            color[index] = 2
            return True

        
        result = []
        for i in range(len(graph)):
            if dfs(i):
                result.append(i)
                
        return result