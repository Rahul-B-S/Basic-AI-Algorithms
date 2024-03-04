from math import inf

board=[" " for i in range(9)]

def board_print(board):
    for i in range(0,9,3):
        print(board[i]+"|"+board[i+1]+"|"+board[i+2])
        if i!=6:
            print("-+-+-")

def check_win(board,player):
    for i in range(0,9,3):
        if board[i]==board[i+1]==board[i+2]==player:
            return True
    for i in range(3):
        if board[i]==board[i+3]==board[i+6]==player:
            return True
    if board[0]==board[4]==board[8]==player:
        return True
    if board[2]==board[4]==board[6]==player:
        return True
    return False

def board_full(board):
    return " " not in board

def minimax(board,depth,is_maximizing):
    if check_win(board,"X"):
        return 1
    if check_win(board,"O"):
        return -1
    if board_full(board):
        return 0
    if is_maximizing:
        best_score=-inf
        for i in range(9):
            if board[i]==" ":
                board[i]="X"
                score=minimax(board,depth+1,False)
                board[i]=" "
                best_score=max(score,best_score)
        return best_score
    else:
        best_score=inf
        for i in range(9):
            if board[i]==" ":
                board[i]="O"
                score=minimax(board,depth+1,True)
                board[i]=" "
                best_score=min(best_score,score)
        return best_score
        
def ai_move(board):
    best_move=-1
    best_score=-inf
    for i in range(9):
        if board[i]==" ":
            board[i]="X"
            score=minimax(board,0,False)
            board[i]=" "
            if score>best_score:
                best_score=score
                best_move=i
    board[best_move]="X"

while True:
    board_print(board)
    
    ai_move(board)
    print("\n")
    board_print(board)

    if check_win(board,"X"):
        print("AI wins")
        break
    
    if board_full(board):
        print("Draw")
        break

    player_move=int(input("Enter the player input(0-8): "))
    if board[player_move]==" ":
        board[player_move]="O"
    else:
        print("Invalid Input")
        continue

    if check_win(board,"O"):
        board_print(board)
        print("You win")
        break
