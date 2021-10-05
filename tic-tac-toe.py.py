# ------ Global Variables -----

#Game board
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

# If game is still going
game_still_going = True

# Who won? Or tie?
winner = None

#Whose turn is it?
current_player = "X"


#Display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# Play a game tic-tac-toe
def play_game():

    #Display initial board

    display_board()
    #While the game is still going
    while game_still_going:

        #Handle a single turn of an arbitrary player
        handle_turn(current_player)

        # check if the game has ended
        check_if_game_over()

        #Flip to the other player
        flip_player()

    #The game has ended
    if winner == "X" or winner == "O":
        print(winner + "  Won!!")
    elif winner == None:
        print("Game Tie!!")


#Handle a single turn of an arbitrary player
def handle_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    valid = False

    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("Position filled! Try a different position.")

    board[position] = player
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():

    #Set up global Variables
    global winner
    #check rows
    row_winner = check_rows()
    #check columns
    column_winner = check_columns()
    #check diagonals
    diagonal_winner = check_diagonals()

    #Get the Winner
    if row_winner:
        #there was a win
        winner = row_winner
    elif column_winner:
        #there was a win
        winner = column_winner
    elif diagonal_winner:
        #there was a win
        winner = diagonal_winner
    else:
        #there was no win
        winner = None
    return


def check_rows():
    # Set up global variables
    global game_still_going
    #check if any of the rows have all of the same value and not empty
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    #If any rows does have a match, flag that there is a win
    if row1 or row2 or row3:
        game_still_going = False
    # Return the winner (X or O)
    if row1:
        return board[0]
    if row2:
        return board[3]
    if row3:
        return board[6]
    return


def check_columns():
    # Set up global variables
    global game_still_going
    #check if any of the columns have all of the same value and not empty
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"
    #If any columns does have a match, flag that there is a win
    if column1 or column2 or column3:
        game_still_going = False
    # Return the winner (X or O)
    if column1:
        return board[0]
    if column2:
        return board[1]
    if column3:
        return board[2]
    return


def check_diagonals():
    # Set up global variables
    global game_still_going
    #check if any of the diagonals have all of the same value and not empty
    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[6] == board[4] == board[2] != "-"
    #If any diagonals does have a match, flag that there is a win
    if diagonal1 or diagonal2:
        game_still_going = False
    # Return the winner (X or O)
    if diagonal1:
        return board[0]
    if diagonal2:
        return board[6]
    return


def check_if_tie():
    #Set up global variables
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    #Set up global variables
    global current_player
    #If the current player was X, change it to O
    if current_player == "X":
        current_player = "O"
    #If the current player was O, change it to X
    elif current_player == "O":
        current_player = "X"
    return


play_game()

#board
# display board
# play game
#handle turn
# check win
#check rows
#check columns
# check diagonalsc
# check tie
#flip player
