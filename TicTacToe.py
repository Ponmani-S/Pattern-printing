board = ['1','2','3','4','5','6','7','8','9']
current = 'X'

def print_board():
    print("\n")
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("--+---+--")
    print("\n")

def check_win():
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    return any(board[a] == board[b] == board[c] for a,b,c in wins)

def play():
    global current
    moves = 0
    while moves < 9:
        print_board()
        move = input(f"Player {current}, enter position (1-9): ")
        if move.isdigit() and int(move) in range(1,10) and board[int(move)-1] not in ['X','O']:
            board[int(move)-1] = current
            moves += 1
            if check_win():
                print_board()
                print(f"Player {current} wins!")
                return
            current = 'O' if current == 'X' else 'X'
        else:
            print("Invalid move. Try again.")
    print_board()
    print("It's a draw!")

play()
