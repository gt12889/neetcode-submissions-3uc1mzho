class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dir = [(-1,0),(1,0),(0,-1),(0,1)]
        visited = set()
        count = 0

        rows = len(grid)
        cols = len(grid[0])

        def bfs(r,c):
            visited.add((r,c))
            q=collections.deque([(r,c)])


            while q:
                row,col = q.popleft()
                for (dr,dc) in dir:
                    pr,pc = row+dr,col+dc
                    if (pr in range(rows) and
                    pc in range(cols) and
                    (pr,pc) not in visited and
                    grid[pr][pc] == "1"):
                        visited.add((pr,pc))
                        q.append((pr,pc))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                     bfs(r,c)
                     count+=1
        return count

