import math

print("")
print("WELCOME! TO THE TIC-TAC-TOE GAME.")
print("")
print("PLEASE FOLLOW THESE INSTRUCTIONS.")
print("")
print("1. You will be playing as X. ")
print("2. The BOT will be playing as O.")
print("3. To make a move, simply type the number of the space where you want to place your piece.")
print("4. The game will end when one player has three in a row, or when all spaces are filled.")
print("5. If all spaces are filled and no player has three in a row, the game is a draw.")

#print the Tic Tac Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

#to check winner
def check_winner(board, player):
    for i in range(3):
        if all([spot == player for spot in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

#TO check draw
def check_draw(board):
    return all([spot != " " for row in board for spot in row])

# player's move
def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("This spot is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")

# Minimax
def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if check_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

#BOT move
def ai_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    if move:
        board[move[0]][move[1]] = "O"

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    while True:
        print_board(board)
        player_move(board)
        if check_winner(board, "X"):
            print_board(board)
            print("CONGRATULATIONS!, YOU WIN! THE GAME.")
            print("")
            print("HOPE YOU ENJOY THE GAME!")
            break
        elif check_draw(board):
            print_board(board)
            print("Ohh! The game is draw!")
            print("")
            print("HOPE YOU ENJOY THE GAME!")
            break

        ai_move(board)
        if check_winner(board, "O"):
            print_board(board)
            print("BOT WIN! THE GAME.")
            print("")
            print("HOPE YOU ENJOY THE GAME!")
            break
        elif check_draw(board):
            print_board(board)
            print("Ohh! The game is draw!")
            print("")
            print("HOPE YOU ENJOY THE GAME!")
            break


play_game()
