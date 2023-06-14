'''
Tictactoe Game
Authors: Efita Effiom & Daniel Nwachukwu
'''
# Prints a welcome message
def main():
    print("Welcome to the Tic-Tac-Toe game!")
    
    # Prompts Player 1 and Player 2 to enter their names
    player1_name = input("Player 1, please enter your name: ")
    player2_name = input("Player 2, please enter your name: ")
    
    # Greets the players and starts the game
    print(f"Hi {player1_name} and {player2_name}! Let's start playing.")

    # Initializes the game
    player = next_player("")
    board = create_board()
    game_count = 0
    
   # Main game loop
    while True:
        game_count += 1
        print(f"Game #{game_count}")
        
        # Game loop for each individual game
        while not (has_winner(board) or is_a_draw(board)):
            
            display_board(board)
            make_move(player, board, player1_name, player2_name)
            player = next_player(player)
        
         # Game ended, display the final board
        display_board(board)
        
        # Determines the winner and displays the result
        winner = get_winner(board, player1_name, player2_name)
        if winner:
            print(f"Congratulations {winner}! You are the winner!")
        else:
            print("It's a draw!")
        
        # Asks the players if they want to play again
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break
        
        # Resets the game for a new round
        board = create_board()
    
    # Game ended, print the total number of games played and say goodbye
    print(f"Total number of games played: {game_count}")
    print("Goodbye!")

def create_board():
    # Creates an empty game board as a list
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

# Displays the current game board
def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()
    
# Checks if the game ended in a draw
def is_a_draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 
    
# Checks if there is a winner in the current game board
def has_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

# Asks the current player to choose a square and makes a move on the board
def make_move(player, board, player1_name, player2_name):
    if player == "x":
        player_name = player1_name
    else:
        player_name = player2_name
    square = int(input(f"{player_name}'s turn to choose a square (1-9): "))
    board[square - 1] = player

# Determines the next player based on the current player
def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

# Determines the winner based on the current game board
def get_winner(board, player1_name, player2_name):
    if has_winner(board):
        if board[0] == board[1] == board[2]:
            return player1_name if board[0] == "x" else player2_name
        elif board[3] == board[4] == board[5]:
            return player1_name if board[3] == "x" else player2_name
        elif board[6] == board[7] == board[8]:
            return player1_name if board[6] == "x" else player2_name
        elif board[0] == board[3] == board[6]:
            return player1_name if board[0] == "x" else player2_name
        elif board[1] == board[4] == board[7]:
            return player1_name if board[1] == "x" else player2_name
        elif board[2] == board[5] == board[8]:
            return player1_name if board[2] == "x" else player2_name
        elif board[0] == board[4] == board[8]:
            return player1_name if board[0] == "x" else player2_name
        elif board[2] == board[4] == board[6]:
            return player1_name if board[2] == "x" else player2_name
    return None

if __name__ == "__main__":
    main()
