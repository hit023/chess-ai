from itertools import count
import chess

A1, H1, A8, H8 = 91, 98, 21, 28
player_turn=1
N, E, S, W = -10, 1, 10, -1
directions = {
    'P': (N, N+N, N+W, N+E),
    'N': (N+N+E, E+N+E, E+S+E, S+S+E, S+S+W, W+S+W, W+N+W, N+N+W),
    'B': (N+E, S+E, S+W, N+W),
    'R': (N, E, S, W),
    'Q': (N, E, S, W, N+E, S+E, S+W, N+W),
    'K': (N, E, S, W, N+E, S+E, S+W, N+W)
}
def fen_to_b(fen):
    b = fen.split()[0]
    b = b.split('/')
    b_str = ('         \n''         \n')
    for line in b:
        s  = " "
        for i in line:
            if i.isalpha():
                s+=i
            else:
                t = int(i)
                for j in range(t):
                    s+="."
        s+='\n'
        b_str+=s
    b_str += ('         \n''         \n')
    return b_str

def generate_moves(fen):
    b = fen_to_b(fen)
    for i, p in enumerate(b):
        if not p.isupper(): continue
        for d in directions[p]:
            for j in count(i+d, d):
                q = b[j]
                # Stay inside the b, and off friendly pieces
                if q.isspace() or q.isupper(): break
                # Pawn move, double move and capture
                if p == 'P' and d in (N, N+N) and q != '.': break
                if p == 'P' and d == N+N and (i < A1+N or b[i+N] != '.'): break
                # Move it
                yield (i-20, j-20)
                # Stop crawlers from sliding, and sliding after captures
                if p in 'PNK' or q.islower(): break

t = generate_moves('r3r1k1/pp3nPp/1b1p1B2/1q1PN2/8/P4Q2/1P3PK1/R6R b KQkq - 0 1')
for i,j in t:
    print(i,j)
