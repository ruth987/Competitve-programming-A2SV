class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        island = []

        # DFS to find all the islands
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return
            grid[r][c] = 0
            island.append((r, c))
            for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                row, col = r + dr, c + dc 
                dfs(row, col)

        islands = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r, c)
                    islands.append(island)
                    island = []

        # BFS to find the shortest distance to the other island
        def shortestPath(queue, visited):
            path = 0
            while queue:
                length = len(queue)
                for _ in range(length):
                    row, col = queue.popleft()
                    for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                        r, c = row + dr, col + dc
                        if r < 0 or c < 0 or c >= cols or r >= rows or (r, c) in visited:
                            continue
                        visited.add((r, c))
                        if (r, c) in islands[1]:
                            return path
                        grid[r][c] = 1
                        queue.append((r, c))
                path += 1

            return 0

        # enqueue all the nodes in the first island
        queue = deque()
        visited = set()
        for r, c in islands[0]:
            queue.append((r, c))
            visited.add((r, c))

        return shortestPath(queue, visited)