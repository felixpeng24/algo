"""
You are given a 2-d matrix where each cell consists of either /, \, or an empty space. Write an algorithm that determines into how many regions the slashes divide the space.

For example, suppose the input for a three-by-six grid is the following:

\    /
 \  /
  \/
Considering the edges of the matrix as boundaries, this divides the grid into three triangles, so you should return 3.



"""

from collections import deque

def regions_by_slashes(grid):
    n = len(grid)
    m = len(grid[0]) if n else 0
    S = 3
    H, W = n*S, m*S
    # 1 = blocked (wall), 0 = empty
    img = [[0]*W for _ in range(H)]

    #created an empty 3N * 3M grid

    for i in range(n):
        for j in range(m):
            c = grid[i][j]
            if c == '/':
                img[i*S + 0][j*S + 2] = 1
                img[i*S + 1][j*S + 1] = 1
                img[i*S + 2][j*S + 0] = 1
            elif c == '\\':
                img[i*S + 0][j*S + 0] = 1
                img[i*S + 1][j*S + 1] = 1
                img[i*S + 2][j*S + 2] = 1
            # spaces leave empty
        
        #blocked out sections with the dashes

    def bfs(sr, sc):
        q = deque([(sr, sc)])
        img[sr][sc] = 1  # mark visited by turning to wall
        while q:
            r, c = q.popleft()
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r+dr, c+dc
                if 0 <= nr < H and 0 <= nc < W and img[nr][nc] == 0:
                    img[nr][nc] = 1
                    q.append((nr, nc))

#kinda genius, flood fill
#check all the spaces around you, NSWE
#BFS with queue, add to queue o spot is 0 or out of the grid
#checking for regions, scan whole grid for spots

    regions = 0
    for r in range(H):
        for c in range(W):
            if img[r][c] == 0:
                regions += 1
                bfs(r, c)
    return regions
