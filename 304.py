"""
HARD

A knight is placed on a given square on an 8 x 8 chessboard. It is then moved randomly several times, where each move is a standard knight move. If the knight jumps off the board at any point, however, it is not allowed to jump back on. After k moves, what is the probability that the knight remains on the board?

"""

def knight_survival_probability(start_r, start_c, k):
    moves = [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]
    N = 8
    q = [[1.0]*N for _ in range(N)]  # t = 0

    for _ in range(k):
        q_next = [[0.0]*N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                s = 0.0
                for dr, dc in moves:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < N and 0 <= nc < N:
                        s += q[nr][nc]
                    # else contributes 0
                q_next[r][c] = s / 8.0
        q = q_next

    return q[start_r][start_c]
