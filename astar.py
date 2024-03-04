import heapq

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

def cost(initial,goal):
    cost=0
    for i in range(3):
        for j in range(3):
            if initial[i][j]!=goal[i][j]:
                cost+=1
    return cost

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

def astar(initial,goal):
    visited=set()
    gn=0
    hn=cost(initial,goal)
    fn=gn+hn
    stack=[(fn,initial,[],[])]
    while stack:
        state,path,moves=heapq.heappop(stack)[1:]
        if state == goal:
            return path,moves
        visited.add(tuple(map(tuple,state)))
        for move in ["up","down","left","right"]:
            if is_valid(state,move):
                new_state=generate(state,move)
                if tuple(map(tuple,new_state)) not in visited:
                    gn=gn+1
                    hn=cost(initial,new_state)
                    fn=gn+hn
                    new_path=path+[new_state]
                    new_move=moves+[move]
                    heapq.heappush(stack,(fn,new_state,new_path,new_move))
    return [],[]

print("Enter the Initial state: ")
initial=mat()
print("Enter the Goal state: ")
goal=mat()
path,moves=astar(initial,goal)
if path:
    print("Steps to reach goal is: ")
    step=1
    for state,move in zip(path,moves):
        print("Step",step," :",move)
        printer(state)
        print()
        step+=1
else:
    print("No solution")
