def convertToAlgebraic(i,j):
    assert((i<=98 and i>=21) and (j<=98 and j>=21)), "invalid position(s)."
    irow = 9-(i/10)+1
    icol = i%10
    ialn = str(chr(ord('a')+icol-1)) + str(irow)

    jrow = 9-(j/10)+1
    jcol = j%10
    jaln = str(chr(ord('a')+jcol-1)) + str(jrow)

    return (ialn,jaln)


pawnEvalWhite = [
        [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
        [5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0],
        [1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0],
        [0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5],
        [0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0],
        [0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5],
        [0.5,  1.0, 1.0,  -2.0, -2.0,  1.0,  1.0,  0.5],
        [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]
    ]

pawnEvalBlack = list(reversed(pawnEvalWhite))

knightEval = [
        [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
        [-4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0],
        [-3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0],
        [-3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0],
        [-3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0],
        [-3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0],
        [-4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0],
        [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]
    ]

bishopEvalWhite = [
    [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
    [ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
    [ -1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0],
    [ -1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0],
    [ -1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0],
    [ -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0],
    [ -1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0],
    [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]
]

bishopEvalBlack = list(reversed(bishopEvalWhite))

rookEvalWhite = [
    [  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
    [  0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [  0.0,   0.0, 0.0,  0.5,  0.5,  0.0,  0.0,  0.0]
]

rookEvalBlack = list(reversed(rookEvalWhite))

evalQueen = [
    [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
    [ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
    [ -1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
    [ -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
    [  0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
    [ -1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
    [ -1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0],
    [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]
]

kingEvalWhite = [
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
    [ -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
    [  2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0 ],
    [  2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0 ]
]

kingEvalBlack = (reversed(kingEvalWhite));

# def evaluateBoard(board):
#     totalEval = 0
#     for i in range(len(board)):
#         totalEval = totalEval + getPieceValue(str(board[i]),i)
#     return totalEval
#
# def getPieceValue(piece,index):
#     if(piece == 'P') :
#         return pst.get('P')[index]
#     elif piece == 'R':
#         return pst.get('R')[index]
#     elif piece == 'N':
#         return pst.get('N')[index]
#     elif piece == 'Q':
#         return pst.get('Q')[index]
#     elif piece == 'K':
#         return pst.get('K')[index]
#     elif piece == 'B':
#         return pst.get('B')[index]
#     else:
#         return 0

def evaluateBoard(board):
    board = board.strip()
    board = board.split('\n')
    i=0
    while i<len(board):
        board[i] = board[i].strip()
        i+=1
    total_eval = 0
    for i in range(8):
        for j in range(8):
            total_eval += getPieceValue(board[i][j],i,j)


            #print(total_eval)
    return total_eval

def getPieceValue(p,i,j):
    if not (p.isalpha()) or not p.isupper():
        return 0
    if p == 'P':
        return 10 + pawnEvalWhite[j][i]
    if p == 'R':
        return 50 + rookEvalWhite[j][i]
    if p == 'N':
        return 30 + knightEval[j][i]
    if p == 'B':
        return 30 + bishopEvalWhite[j][i]
    if p == 'Q':
        return 90 + evalQueen[j][i]
    if p == 'K':
        return 900 + kingEvalWhite[j][i]

def value( i,j, board):
    #print(i)
    score = 0
    #print(board)
    p = board[i]
    #print("in value(), i: "+str(i))
    #print("p: "+ p)
    if not p.isalpha():
        return 0
    q = board[j]
    if q.islower():
        #print("it is a capture!")
        #print(i,j)
        board = list(board)
        board[j] = 'A'
        board = "".join(board)
        board = board.strip()
        board = board.split('\n')
        i=0
        while i<len(board):
            board[i] = board[i].strip()
            i+=1
        idxi,idxj = 0,0
        for i in range(8):
            for k in range(8):
                if board[i][k]=='A':
                    idxi,idxj = i,k
                    break
        score += getPieceValue(q,idxi,idxj)

    else:
        return 0
    return score

def material(board_state, weight):
    black_points = 0
    board_state = board_state.split()[0]
    piece_values = {'p': 1, 'b': 3, 'n': 3, 'r': 5, 'q': 9, 'k': 0}
    for piece in board_state:
        if piece.islower():
            black_points += piece_values[piece]
        elif piece.isupper():
            black_points -= piece_values[piece.lower()]
    return black_points * weight

def piece_moves(game, weight):
    black_points = 0
    turn = str(game).split()[1]
    square_values = {"e4": 1, "e5": 1, "d4": 1, "d5": 1, "c6": 0.5, "d6": 0.5, "e6": 0.5, "f6": 0.5,
                    "c3": 0.5, "d3": 0.5, "e3": 0.5, "f3": 0.5, "c4": 0.5, "c5": 0.5, "f4": 0.5, "f5": 0.5}
    possible_moves = game.get_moves()
    for move in possible_moves:
        if turn == "b":
            if move[2:4] in square_values:
                black_points += square_values[move[2:4]]
        else:
            if move[2:4] in square_values:
                black_points -= square_values[move[2:4]]
    # piece_values = {'p': 1, 'b': 4, 'n': 4, 'r': 3, 'q': 3, 'k': 0}
    # for move in game.get_moves():
    #     current_piece = game.board.get_piece(game.xy2i(move[:2]))
    #     if current_piece.islower():
    #         black_points += piece_values[current_piece]
    return black_points
