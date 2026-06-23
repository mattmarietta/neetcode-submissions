class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Given a 2d matrix grid
        # 0 - emtpy cell
        # 1 - fresh fruit
        # 2 - rotten fruit
        # If a 1 is horizontally or vertically adjacent to a rotten fruit then the fresh fruit becomes rotten
        # 1 horizontal or vertical next to a 2 then become a 2
        # Min number of minutes must elapse for zero fresh fruits

        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        # Use BFS to track the levels of fresh fruit visited
        rows = len(grid)
        cols = len(grid[0])
        fresh_oranges = 0
        minMinutes = 0 
        
        q = collections.deque()
        # while q exists


        # Need to start bfs at all rotten fruit
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        while q and fresh_oranges > 0:
            length = len(q)
            # Go through each of the rotten oranges
            for i in range(length):
                row, col = q.popleft()

                for dr, dc in DIRECTIONS:
                    nr = dr + row
                    nc = dc + col
                    if (nr in range(len(grid)) and nc in range(len(grid[0])) and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh_oranges -= 1
            minMinutes += 1
        if fresh_oranges == 0:
            return minMinutes
        return -1

