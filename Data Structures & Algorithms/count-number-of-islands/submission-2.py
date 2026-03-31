class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dir = [[-1,0],[0,1],[0,-1],[1,0]]
        count = 0
        visited = set()
        rows,cols = len(grid),len(grid[0])

        def bfs(r,c):
            dr,dc = 0,0
            q = collections.deque([(r,c)])
            visited.add((r,c))
            while q:
                row,col = q.popleft()
                for [dr,dc] in dir:
                    pr,pc = row+dr, col+dc
                    if (pr in range(rows) and
                    pc in range(cols) and
                    grid[pr][pc] == "1" and
                    (pr,pc) not in visited):
                        visited.add((pr,pc))
                        q.append((pr,pc))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row,col) not in visited:
                    bfs(row,col)
                    count+=1
        return count