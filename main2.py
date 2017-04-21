import chess
import chess.polyglot
import heuristics
from collections import namedtuple
from itertools import count

MATE_LOWER = 60000 - 8*2700
MATE_UPPER = 60000 + 8*2700


#assume AI plays white

initial = (
    '         \n'  #   0 -  9
    '         \n'  #  10 - 19
    ' rnbqkbnr\n'  #  20 - 29
    ' pppppppp\n'  #  30 - 39
    ' ........\n'  #  40 - 49
    ' ........\n'  #  50 - 59
    ' ........\n'  #  60 - 69
    ' ........\n'  #  70 - 79
    ' PPPPPPPP\n'  #  80 - 89
    ' RNBQKBNR\n'  #  90 - 99
    '         \n'  # 100 -109
    '         \n'  # 110 -119
)


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

A1, H1, A8, H8 = 91, 98, 21, 28

pst = {
    'P': (0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 198, 198, 198, 198, 198, 198, 198, 198, 0,
        0, 178, 198, 198, 198, 198, 198, 198, 178, 0,
        0, 178, 198, 198, 198, 198, 198, 198, 178, 0,
        0, 178, 198, 208, 218, 218, 208, 198, 178, 0,
        0, 178, 198, 218, 238, 238, 218, 198, 178, 0,
        0, 178, 198, 208, 218, 218, 208, 198, 178, 0,
        0, 178, 198, 198, 198, 198, 198, 198, 178, 0,
        0, 198, 198, 198, 198, 198, 198, 198, 198, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    'B': (0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 797, 824, 817, 808, 808, 817, 824, 797, 0,
        0, 814, 841, 834, 825, 825, 834, 841, 814, 0,
        0, 818, 845, 838, 829, 829, 838, 845, 818, 0,
        0, 824, 851, 844, 835, 835, 844, 851, 824, 0,
        0, 827, 854, 847, 838, 838, 847, 854, 827, 0,
        0, 826, 853, 846, 837, 837, 846, 853, 826, 0,
        0, 817, 844, 837, 828, 828, 837, 844, 817, 0,
        0, 792, 819, 812, 803, 803, 812, 819, 792, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    'N': (0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 627, 762, 786, 798, 798, 786, 762, 627, 0,
        0, 763, 798, 822, 834, 834, 822, 798, 763, 0,
        0, 817, 852, 876, 888, 888, 876, 852, 817, 0,
        0, 797, 832, 856, 868, 868, 856, 832, 797, 0,
        0, 799, 834, 858, 870, 870, 858, 834, 799, 0,
        0, 758, 793, 817, 829, 829, 817, 793, 758, 0,
        0, 739, 774, 798, 810, 810, 798, 774, 739, 0,
        0, 683, 718, 742, 754, 754, 742, 718, 683, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    'R': (0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 1258, 1263, 1268, 1272, 1272, 1268, 1263, 1258, 0,
        0, 1258, 1263, 1268, 1272, 1272, 1268, 1263, 1258, 0,
        0, 1258, 1263, 1268, 1272, 1272, 1268, 1263, 1258, 0,
        0, 1258, 1263, 1268, 1272, 1272, 1268, 1263, 1258, 0,
        0, 1258, 1263, 1268, 1272, 1272, 1268, 1263, 1258, 0,
        0, 1258, 1263, 1268, 1272, 1272, 1268, 1263, 1258, 0,
        0, 1258, 1263, 1268, 1272, 1272, 1268, 1263, 1258, 0,
        0, 1258, 1263, 1268, 1272, 1272, 1268, 1263, 1258, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    'Q': (0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 2529, 2529, 2529, 2529, 2529, 2529, 2529, 2529, 0,
        0, 2529, 2529, 2529, 2529, 2529, 2529, 2529, 2529, 0,
        0, 2529, 2529, 2529, 2529, 2529, 2529, 2529, 2529, 0,
        0, 2529, 2529, 2529, 2529, 2529, 2529, 2529, 2529, 0,
        0, 2529, 2529, 2529, 2529, 2529, 2529, 2529, 2529, 0,
        0, 2529, 2529, 2529, 2529, 2529, 2529, 2529, 2529, 0,
        0, 2529, 2529, 2529, 2529, 2529, 2529, 2529, 2529, 0,
        0, 2529, 2529, 2529, 2529, 2529, 2529, 2529, 2529, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    'K': (0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 60098, 60132, 60073, 60025, 60025, 60073, 60132, 60098, 0,
        0, 60119, 60153, 60094, 60046, 60046, 60094, 60153, 60119, 0,
        0, 60146, 60180, 60121, 60073, 60073, 60121, 60180, 60146, 0,
        0, 60173, 60207, 60148, 60100, 60100, 60148, 60207, 60173, 0,
        0, 60196, 60230, 60171, 60123, 60123, 60171, 60230, 60196, 0,
        0, 60224, 60258, 60199, 60151, 60151, 60199, 60258, 60224, 0,
        0, 60287, 60321, 60262, 60214, 60214, 60262, 60321, 60287, 0,
        0, 60298, 60332, 60273, 60225, 60225, 60273, 60332, 60298, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
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

def board_to_fen(board):
    fen = ''
    board = ' '+board.strip() + '\n'
    i=0
    while i < len(board):
        if board[i].isspace():
            i+=1
            continue
        elif board[i].isalpha():
            fen+=board[i]
            i+=1
        elif board[i]=='.':
            count=0
            while board[i]=='.':
                count+=1
                i+=1
            fen+=str(count)
        if board[i] == '\n':
            fen += '/'
            i += 1

    return fen[:-1]

def convert_to_sfindices(move):
    start = move[0] + move[1]
    end = move[2] + move[3]
    i = ord(start[0])-ord('a')+1 + 100-10*int(start[1])
    j = ord(end[0])-ord('a')+1 + 100-10*int(end[1])
    return (i,j)

def convertToAlgebraic(i,j):
    assert((i<=98 and i>=21) and (j<=98 and j>=21)), "invalid position(s)."
    irow = 9-(i/10)+1
    icol = i%10
    ialn = str(chr(ord('a')+icol-1)) + str(irow)

    jrow = 9-(j/10)+1
    jcol = j%10
    jaln = str(chr(ord('a')+jcol-1)) + str(jrow)

    return (ialn,jaln)


class Node():
    def __init__(self, board_state=None, algebraic_move=None, value=None):
        self.board_state = board_state #fen representation
        self.algebraic_move = algebraic_move #e2e4

class AI(object):
    def __init__(self,max_depth=4,node_count=0):
        self.max_depth = max_depth
        #self.leaf_nodes = heuristic_gen(leaf_nodes)
        #self.pos = pos
        self.node_count = node_count

    def apply_move(self,possible_moves,board_state):
        possible_moves_updated = []
        for n in possible_moves:#every tuple
            #push the move and update the board
            #board_state is in fen
            b = fen_to_board(board_state)
            i,j = n
            p,q = b[i],b[j]
            put = lambda board, i, p: board[:i] + p + board[i+1:]
            b = put(b, j, b[i])
            b = put(b, i, '.')
            k = Node(board_to_fen(b),''.join(convertToAlgebraic(i,j)))
            possible_moves_updated.append(k)
        return possible_moves_updated

    def get_moves(self,fen):
        global player_turn
        b = fen_to_board(fen)
        for i,p in enumerate(b):
            if not p.isupper(): continue
            for d in directions[p]:
                for j in count(i+d, d):
                    q = b[j]
                    if q.isspace() or q.isupper(): break
                    if p == 'P' and d in (N, N+N) and q != '.':
                        break
                    if p == 'P' and d == N+N and (i < A1+N or b[i+N] != '.'):
                        break #double move by the pawn only in the first turn.
                    yield (i, j)
                    if p in 'PNK' or q.islower():
                        break

    def ab_make_move(self, board_state):
        possible_moves = list(self.get_moves(board_state))
        possible_moves_updated = self.apply_move(possible_moves,board_state)
        alpha = float("-inf")
        beta = float("inf")
        best_move = possible_moves_updated[0]
        for move in possible_moves_updated:
            #move = Node(board_state,''.join(convertToAlgebraic(move[0],move[1])))
            board_value = self.ab_minimax(move, alpha, beta, 1)
            if alpha < board_value:
                alpha = board_value
                best_move = move
                best_move.value = alpha
        # best_move at this point stores the move with the highest heuristic
        return best_move.algebraic_move

    def ab_minimax(self, node, alpha, beta, current_depth=0):
        current_depth += 1
        #base case to stop recursion, ie: when max_depth is reached.
        if current_depth == self.max_depth:
            board_value = self.get_heuristic(node.board_state)
            #move = convert_to_sfindices(node.algebraic_move)
            #board_value = self.value(move,fen_to_board(node.board_state))
            if current_depth % 2 == 0:
                # pick largest number, where root is black and even depth
                if (alpha < board_value):
                    alpha = board_value
                self.node_count += 1
                return alpha
            else:
                # pick smallest number, where root is black and odd depth
                if (beta > board_value):
                    beta = board_value
                self.node_count += 1
                return beta

        possible_moves = list(self.get_moves(node.board_state))
        #for i,move in enumerate(possible_moves):
        #    clone = node.board_state #fen
        #    node = Node(clone)
        #    node.algebraic_move = convertToAlgebraic(move[0],move[1])
        #    possible_moves[i] = node

        possible_moves = self.apply_move(possible_moves,node.board_state)
        #print("exploring: "+node.algebraic_move)
        if current_depth % 2 == 0:
            # min player's turn
            for child_node in possible_moves:
                #print("child move: "+child_node.algebraic_move)
                if alpha < beta:
                    board_value = self.ab_minimax(child_node,alpha, beta, current_depth)
                    if beta > board_value:
                        beta = board_value
            return beta
        else:
            # max player's turn
            for child_node in possible_moves:
                if alpha < beta:
                    board_value = self.ab_minimax(child_node,alpha, beta, current_depth)
                    if alpha < board_value:
                        alpha = board_value
            return alpha

    def get_heuristic(self, board_state=None):
        total_points = 0
        # total piece count
        total_points += heuristics.evaluateBoard(fen_to_board(board_state))
        #total_points += heuristics.material(board_state, 100)
        return total_points

    def value(self, move,board):
        i, j = move
        p, q = board[i], board[j]
        # Actual move
        score = 0
        score = pst[p][j] - pst[p][i]
        # Capture
        if q.islower():
            score += pst[q.upper()][119-j]
        return score

class Position(namedtuple('Position', 'board score wc bc')):

        def move(self, move):
            global player_turn
            i, j = move
            p, q = self.board[i], self.board[j]
            put = lambda board, i, p: board[:i] + p + board[i+1:]
            # Copy variables and reset ep and kp
            board = self.board
            wc, bc = self.wc, self.bc
            score = self.score
            if(player_turn==1):
                score = self.score + self.value(move)
            # Actual move
            board = put(board, j, board[i])
            board = put(board, i, '.')
            return Position(board, score, wc, bc)

        def value(self, move):
            i, j = move
            p, q = self.board[i], self.board[j]
            score = pst[p][j] - pst[p][i]
            if q.islower():
                score += pst[q.upper()][119-j]
            return score

def main():
    global player_turn
    board = chess.Board()
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

#AI starts, opening book exhausted.
    boardsf = board.board_fen()
    board = fen_to_board(boardsf)
    pos = Position(board, 0, (True,True), (True,True))
    ai = AI()
    player_turn = 0
    while True:
        while True:
            black_move = raw_input("Enter starting and ending positons(example: e2e4):\n")
            black_move.strip()
            try:
                assert len(black_move)==4,"Invalid format!"
            except AssertionError:
                continue
            pos = pos.move(convert_to_sfindices(black_move))
            print(pos.board)

            player_turn = 1

            node = Node(board_to_fen(pos.board),black_move)
            move = ai.ab_make_move(node.board_state)
            print("My mov: " + move)
            pos = pos.move(convert_to_sfindices(move))
            print(pos.board)

            player_turn = 0


if __name__ == '__main__':
    main()
