def is_attacking(i,j):
    for k in range(4):
        if board[i][k]==1 or board[k][j]==1:
            return True
    for k in range(4):
        for l in range(4):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]==1:
                    return True
    return False


def queens(n,row,solutions):
    if row==n:
        solutions.append([list(row) for row in board])
        return True
    for col in range(n):
        if not(is_attacking(row,col)):
            board[row][col]=1
            queens(n,row+1,solutions)
            board[row][col]=0
    return False

board=[[0]*4 for i in range(4)]
solutions=[]
queens(4,0,solutions)
print("The solution is: ")
for solution in solutions:
    for i in range(4):
        l=solution[i]
        print("\n+--+--+--+--+")
        print("|",end="")
        for j in l:
            if j==0:
                print("  ",end="")
            else:
                print("Q"+str(i+1),end="")
            print("|",end="")
    print("\n+--+--+--+--+")

