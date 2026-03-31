class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows , cols = len(grid),len(grid[0])
        count = 0
        seen = []

        def bfs(r,c):
            dir = [[-1,0],[1,0], [0,-1],[0,1]]
            seen.append([r,c])
            queue = collections.deque()

            queue.append((r,c))
            
            while queue:
                curr_r, curr_c=queue.popleft()
                
                for dr,dc in dir:
                    row, col = curr_r+dr,curr_c+dc
                    if (row in range(rows) and
                        col in range(cols) and
                    [row, col] not in seen and
                        grid[row][col] == "1"):
                        queue.append((row,col))
                        seen.append([row,col])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and [r,c] not in seen:
                    bfs(r,c)
                    count+=1
        return count


