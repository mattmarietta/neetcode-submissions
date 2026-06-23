class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Idea is to check all edges vertically and horizontally
        #Loop through the list

        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        # Make our breadth first search function
        def bfs(r, c):
            # Use a queue to store the places we have visited
            q = collections.deque()
            grid[r][c] = "0"
            q.append((r, c))
            while q:
                row , col = q.popleft()
                for dr, dc in DIRECTIONS:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == "0"):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = "0"

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        return islands