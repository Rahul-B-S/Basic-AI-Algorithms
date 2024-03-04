def mat():
    mat=[]
    for i in range(3):
        mat.append(input().split(" "))
    return mat

def printer(mat):
    for i in mat:
        for j in i:
            print(j,end=" ")
        print()

def posfind(mat):
    l=[]
    for i in range(3):
        for j in range(3):
            if mat[i][j]=="0":
                l.append(i)
                l.append(j)
                break
    return l

def is_valid(mat,move):
    position=posfind(mat)
    row,col=position[0],position[1]
    if move=="up" and row>0:
        return True
    elif move=="down" and row<2:
        return True
    elif move=="left" and col>0:
        return True
    elif move=="right" and col<2:
        return True
    else:
        return False

def generate(mat,move):
    position=posfind(mat)
    row,col=position[0],position[1]
    newmat=[list(i) for i in mat]
    if move=="up":
        newmat[row][col],newmat[row-1][col]=newmat[row-1][col],newmat[row][col]
    elif move=="down":
        newmat[row][col],newmat[row+1][col]=newmat[row+1][col],newmat[row][col]
    elif move=="right":
        newmat[row][col],newmat[row][col+1]=newmat[row][col+1],newmat[row][col]
    elif move=="left":
        newmat[row][col],newmat[row][col-1]=newmat[row][col-1],newmat[row][col]
    return newmat
def dfs(initail,goal):
    visited=set()
    stack=[initial]
    while stack:
        node=stack.pop()
        if node==goal:
            print("Goal state Found")
            printer(node)
            break
        visited.add(tuple(map(tuple,node)))
        for move in ["up","down","left","right"]:
            if is_valid(node,move):
                newmat=generate(node,move)
                if tuple(map(tuple,newmat)) not in visited:
                    stack.append(newmat)
                    print("Move: ",move)
                    printer(newmat)
                    print("\n")
print("Enter the Initial state: ")
initial=mat()
print("Enter the Goal state: ")
goal=mat()
dfs(initial,goal)
