import numpy as np
import streamlit as st
EMPTY = -1
BLACK = 0
WHITE = 1
DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
class Othello:
    EMPTY = -1
    BLACK = 0
    WHITE = 1
    DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def __init__(self, board):
        self.x = 0
        self.tomper = 0
        # with open(filename) as f:
        #     self.turn = int(f.readline().strip())
        #     self.board = [list(map(int, f.readline().split())) for _ in range(8)]
        self.turn=0
        self.board=board
        self.winner = -1

    def change(self, n):
        return 1 - n

    def decision_tree(self, board, player, k, limit, scoreeeee):
        if k == limit:
            return self.get_score(board)
        movesindex = self.get_possible_movesindex(board, player)
        if not movesindex and k != limit:
            tempBoard = self.copy_board(board)
            nn = self.get_score(tempBoard)
            return self.decision_tree(tempBoard, self.change(player), k + 1, limit, scoreeeee)
        
        rootValue = 0
        for i, move in enumerate(movesindex):
            tempBoard = self.copy_board(board)
            o, j = move
            tempBoard[o][j] = player
            self.flip_discs(tempBoard, o, j, player)
            nn = self.decision_tree(tempBoard, self.change(player), k + 1, limit, scoreeeee)
            if i == 0:
                rootValue = nn
            if k == 0:
                scoreeeee.append(nn)
            rootValue = max(rootValue, nn) if player == self.BLACK else min(rootValue, nn)
        return rootValue

    def get_possible_movesindex(self, currentBoard, player):
        moves = []
        for i in range(8):
            for j in range(8):
                if currentBoard[i][j] == self.EMPTY and self.is_valid_move(currentBoard, i, j, player):
                    moves.append((i, j))
        return moves

    def copy_board(self, board):
        return [row[:] for row in board]

    def is_valid_move(self, board, row, col, player):
        if board[row][col] != self.EMPTY:
            print("spso nlkn")
            return False
        for direction in self.DIRECTIONS:
            r, c = row + direction[0], col + direction[1]
            valid = False
            while 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] == self.EMPTY:
                    break
                if board[r][c] == player:
                    if valid:
                        return True
                    else:
                        break
                valid = True
                r += direction[0]
                c += direction[1]
        return False

    def flip_discs(self, board, row, col, player):
        for direction in self.DIRECTIONS:
            r, c = row + direction[0], col + direction[1]
            flip = False
            while 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] == self.EMPTY:
                    break
                if board[r][c] == player:
                    flip = True
                    break
                r += direction[0]
                c += direction[1]
            if flip:
                r, c = row + direction[0], col + direction[1]
                while board[r][c] != player:
                    board[r][c] = player
                    r += direction[0]
                    c += direction[1]

    def get_score(self, board):
        blackScore = sum(row.count(self.BLACK) for row in board)
        whiteScore = sum(row.count(self.WHITE) for row in board)
        return blackScore - whiteScore

    def board_score(self):
        t = self.get_score(self.board)
        return t if self.turn == self.BLACK else -t

    def best_movehelper(self, k):
        scoree = []
        bestScore = self.decision_tree(self.board, self.turn, 0, k, scoree)
        possibleMoves = self.get_possible_movesindex(self.board, self.turn)
        ans = next(i for i, v in enumerate(scoree) if v == bestScore)
        bestMove = 8 * possibleMoves[ans][0] + possibleMoves[ans][1]
        bestMove = min(bestMove, min(8 * move[0] + move[1] for i, move in enumerate(possibleMoves) if scoree[i] == bestScore))
        tempBoard = self.copy_board(self.board)
        row, col = bestMove // 8, bestMove % 8
        tempBoard[row][col] = self.turn
        self.flip_discs(tempBoard, row, col, self.turn)
        self.board = tempBoard
        return bestMove

    def best_move(self, k):
        scoree = []
        bestScore = self.decision_tree(self.board, self.turn, 0, k, scoree)
        possibleMoves = self.get_possible_movesindex(self.board, self.turn)
        ans = next(i for i, v in enumerate(scoree) if v == bestScore)
        bestMove = 8 * possibleMoves[ans][0] + possibleMoves[ans][1]
        return bestMove

    def full_game(self, k):
        ans = []
        i = 0
        while True:
            if i == 2:
                break
            if self.get_possible_movesindex(self.board, self.turn):
                i = 0
                ans.append(self.best_movehelper(k))
                self.turn = self.change(self.turn)
            else:
                i += 1
                self.turn = self.change(self.turn)
        self.winner = self.BLACK if self.get_score(self.board) > 0 else self.WHITE
        return ans

    def get_board_copy(self):
        return self.copy_board(self.board)

    def get_winner(self):
        return self.winner

    def get_turn(self):
        return self.turn

    def print_board(self, board=None):
        if board is None:
            board = self.board
        print("  " + " ".join(map(str, range(8))))
        for i, row in enumerate(board):
            print(i, " ".join("B" if cell == self.BLACK else "W" if cell == self.WHITE else "-" for cell in row))

# Usage example:
# o1 = Othello("ipp.txt")
# o1.print_board()
# print(o1.full_game(3))
def flip_discy(board, row, col, player):
    for direction in DIRECTIONS:
        r, c = row + direction[0], col + direction[1]
        flip = False
        while 0 <= r < 8 and 0 <= c < 8:
            if board[r][c] == EMPTY:
                break
            if board[r][c] == player:
                flip = True
                break
            r += direction[0]
            c += direction[1]
        if flip:
            r, c = row + direction[0], col + direction[1]
            while board[r][c] != player:
                board[r][c] = player
                r += direction[0]
                c += direction[1]
class BoardDisplay:
    BLACK = 0
    WHITE = 1

    def __init__(self):
        # Sample 8x8 board; adjust as needed
        self.board = [[0 for _ in range(8)] for _ in range(8)]
        # Example pieces
        self.board[0][0] = self.BLACK
        self.board[1][1] = self.WHITE

    def print_board(self, board, placeholder):
        # Clear the placeholder and display the board
        with placeholder.container():
            # Clear previous content
            # st.empty() 
            # Create the board layout
            for row in board:
                cols = st.columns(8)  # Create 8 columns for each row
                for j, cell in enumerate(row):
                    cols[j].write("B" if cell == self.BLACK else "W" if cell == self.WHITE else "-")

matrix=[]
for i in range(8):
    u=[]
    for j in range(8):
        u.append(-1)
    matrix.append(u)
matrix[3][3]=0
matrix[4][4]=0
matrix[4][3]=1
matrix[3][4]=1
game=Othello(matrix)
st.title("Big Boss Othello Player")
st.text("[ B:Black , W:White (Yours) ]                      Game Starts with Computer's turn")

if 'game' not in st.session_state:
    st.session_state.game = Othello(matrix)  # Initialize the game with the board matrix
    st.session_state.board_placeholder = st.empty()
    st.session_state.turn = st.session_state.game.turn
    st.session_state.user_turn = False  # Track if it’s the user’s turn
    st.session_state.k = None 
    
if st.session_state.k is None:
    difficulty_options = [2, 3, 4, 5]  # Difficulty options
    st.session_state.k = st.selectbox("Select difficulty:", difficulty_options)
    
def display_board(game):
    printing = BoardDisplay()
    printing.print_board(game.board, st.session_state.board_placeholder)
    
display_board(st.session_state.game)

st.header("Start Game with computer's turn")

if st.button("Ask for computer's turn") and not st.session_state.user_turn:
    st.session_state.game.best_movehelper(st.session_state.k)
    st.session_state.turn = st.session_state.game.change(st.session_state.turn)  # Switch to user’s turn
    st.session_state.user_turn = True  # Now it’s the user’s turn
    
display_board(st.session_state.game)

# Check if it's the user's turn
if st.session_state.user_turn:
    # Row and column inputs for the user
    row = st.number_input("Enter row number (starting from 0 to 7):", min_value=0, max_value=7)
    col = st.number_input("Enter col. number (starting from 0 to 7):", min_value=0, max_value=7)

    if st.button("Place your piece"):
        # Place the user's piece if the move is valid
        if st.session_state.game.is_valid_move(st.session_state.game.board, row, col, st.session_state.turn):
            st.session_state.game.board[row][col] = st.session_state.game.WHITE  # Assuming user plays as WHITE
            st.session_state.game.flip_discs(st.session_state.game.board, row, col, st.session_state.turn)
            st.session_state.turn = st.session_state.game.change(st.session_state.turn)  # Switch to computer’s turn
            st.session_state.user_turn = False  # Next turn is computer’s
        else:
            st.error("Invalid Move")
display_board(st.session_state.game)