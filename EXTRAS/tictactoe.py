'''
Tictactoe Game
Authors: Efita Effiom & Daniel Nwachukwu
'''

def main():
    print("Welcome to the Tic-Tac-Toe game!")
    player1_name = input("Player 1, please enter your name: ")
    player2_name = input("Player 2, please enter your name: ")
    print(f"Hi {player1_name} and {player2_name}! Let's start playing.")

    player = next_player("")
    board = create_board()
    game_count = 0
    
    while True:
        game_count += 1
        print(f"Game #{game_count}")
        
        while not (has_winner(board) or is_a_draw(board)):
            display_board(board)
            make_move(player, board, player1_name, player2_name)
            player = next_player(player)
        
        display_board(board)
        winner = get_winner(board, player1_name, player2_name)
        if winner:
            print(f"Congratulations {winner}! You are the winner!")
        else:
            print("It's a draw!")
        
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break
        
        board = create_board()
    
    print(f"Total number of games played: {game_count}")
    print("Goodbye!")

def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()
    
def is_a_draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 
    
def has_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def make_move(player, board, player1_name, player2_name):
    if player == "x":
        player_name = player1_name
    else:
        player_name = player2_name
    square = int(input(f"{player_name}'s turn to choose a square (1-9): "))
    board[square - 1] = player

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

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
