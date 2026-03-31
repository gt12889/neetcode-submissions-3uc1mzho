class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dir = [[-1,0],[0,1],[1,0],[0,-1]]
        count = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r,c):
            q = collections.deque([(r,c)])
            visited.add((r,c))
            row, col = r,c
            
            while q:
                row,col = q.popleft()
                for [pr,pc] in dir:
                    pr,pc = row+pr,col+pc
                    if (pr in range(rows) and
                    pc in range(cols) and
                    (pr,pc) not in visited and
                    grid[pr][pc] == "1"):
                        visited.add((pr,pc))
                        q.append((pr,pc))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    count+=1
        return count