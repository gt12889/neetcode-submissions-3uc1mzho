class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        di = [(-1,0),(1,0),(0,1),(0,-1)]
        rows,cols = len(heights),len(heights[0])


        pa = [[False] * cols for i in range(rows)]
        atl = [[False] * cols for i in range(rows)]

        def bfs(soruce, ocean):
            q= deque(soruce)
            while q:
                r,c =q.popleft()
                ocean[r][c] = True
                for dr, dc in di:
                    nr,nc = r+dr,c+dc
                    if(0<= nr< rows and 0 <= nc<cols and
                        not ocean[nr][nc] and 
                        heights[nr][nc] >= heights[r][c]):

                        q.append((nr,nc))
        pac = []
        atla = []

        for c in range(cols):
            pac.append((0,c))
            atla.append((rows-1,c))
        
        for r in range(rows):
            pac.append((r,0))
            atla.append((r,cols-1))
        
        bfs(pac,pa)
        bfs(atla,atl)

        res = []

        for r in range(rows):
            for c in range(cols):
                if pa[r][c] and atl[r][c]:
                    res.append([r,c])
        return res