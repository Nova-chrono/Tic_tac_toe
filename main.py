# Tic_Tac_Toe
print('Tic Tac Toe')

board = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-"
]

game_still_running = True   # if game still running

winner = None   # Who wins

current_player = "X" # first player gets X


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
    display_board() # Displays the board

    while game_still_running:
        turns(current_player)

        check_game_over()

        player_flip()

    if winner == "X" or winner == "O":
        print(winner + " " + "won.")
    elif winner == None:
        print("Tie.")


def turns(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    board_positions = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    position_valid = False

    while not position_valid:

        while position not in board_positions:
            position = input("Invalid input!. Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            position_valid = True
        else:
            print("You can't play there." + " " + player + " " + "to play again.")

    board[position] = player
    display_board()


def check_game_over():
    check_win()
    check_tie()


def check_win():
    global winner

    row_win = check_rows()
    col_win = check_columns()
    diag_win = check_diagonals()

    if row_win:
        winner = row_win
    elif col_win:
        winner = col_win
    elif diag_win:
        winner = diag_win
    else:
        winner = None
    return


def check_rows():
    global game_still_running

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_running = False
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return

def check_columns():
    global game_still_running

    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"

    if col_1 or col_2 or col_3:
        game_still_running = False
    if col_1:
        return board[0]
    if col_2:
        return board[1]
    if col_3:
        return board[2]
    return

def check_diagonals():
    global game_still_running

    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[2] == board[4] == board[6] != "-"

    if diag_1 or diag_2:
        game_still_running = False
    if diag_1:
        return board[0]
    if diag_2:
        return board[2]
    return


def check_tie():
    global game_still_running
    
    if "-" not in board:
        game_still_running = False
    return


def player_flip():
    global current_player
    
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


play_game()


#  board
# display board
# play game
# handle turn
# check win
    # check rows
    # check columns
    # check diagonals
# check tie
# flip player