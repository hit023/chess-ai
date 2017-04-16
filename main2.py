import chess.polyglot

board = chess.Board()
#assume AI plays white

player_turn = 1 # 1:white, 0:black
N, E, S, W = -10, 1, 10, -1
directions = {
    'P': (N, N+N, N+W, N+E),
    'N': (N+N+E, E+N+E, E+S+E, S+S+E, S+S+W, W+S+W, W+N+W, N+N+W),
    'B': (N+E, S+E, S+W, N+W),
    'R': (N, E, S, W),
    'Q': (N, E, S, W, N+E, S+E, S+W, N+W),
    'K': (N, E, S, W, N+E, S+E, S+W, N+W)
}

def fen_to_board(fen):
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
    b = fen_to_board(fen)
    if player_turn == 1:
        for i,p in enumerate(b):
            if not p.isspace() and p!='.' and p!='\n' and not p.islower():
                for d in directions[p]:
                    for j in count(i+d, d):
                        q = b[j]
                        if p == 'P' and d in (N, N+N) and q != '.':
                            break
                        if p == 'P' and d == N+N and (i < A1+N or board[i+N] != '.'):
                            break #double move by the pawn only in the first turn.
                        yield (i, j)
                        if p in 'PNK' or q.islower():
                            break


def search(board):
    #MTD
    


def main():
    with chess.polyglot.open_reader("./performance.bin") as reader:
        while True:
            try:
                if player_turn==1:
                    move = reader.find(board)
                    print("move selected: " + str(move.move()) + '\n')
                    board.push(move.move())
                    player_turn = 0
                else:
                    black_move = raw_input("Enter starting and ending positons(example: e2e4):\n")
                    black_move.strip()
                    try:
                        assert len(black_move)==4,"Invalid format!"
                    except AssertionError:
                        continue
                    try:
                        from_square = chess.SQUARE_NAMES.index(black_move[:2])
                        to_square = chess.SQUARE_NAMES.index(black_move[2:])
                    except:
                        print("Invalid Move!")
                        continue
                    black_move = chess.Move(from_square,to_square,promotion=None)
                    board.push(black_move)
                    player_turn = 1
                print(board)
            except IndexError:
                print("All opening moves exhausted!\n")
                break
