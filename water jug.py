def filla(jug):
    jugc=jug.copy()
    jugc[0]=a
    return jugc

def fillb(jug):
    jugc=jug.copy()
    jugc[1]=b
    return jugc

def draina(jug):
    jugc=jug.copy()
    jugc[0]=0
    return jugc

def drainb(jug):
    jugc=jug.copy()
    return jugc

def drainb(jug):
    jugc=jug.copy()
    jugc[1]=0
    return jugc

def a2b(jug):
    jugc=jug.copy()
    rem=b-jugc[1]
    if jugc[0]>rem:
        jugc[0]-=rem
        jugc[1]=b
    else:
        jugc[1]+=jugc[0]
        jugc[0]=0
    return jugc

def b2a(jug):
    jugc=jug.copy()
    rem=a-jugc[0]
    if jugc[1]>rem:
        jugc[1]-=rem
        jugc[0]=a
    else:
        jugc[0]+=jugc[1]
        jugc[1]=0
    return jugc

a=int(input("Enter the size of jugA:"))
b=int(input("Enter the size of jugB:"))
target=int(input("Enter the target size:"))
moves=[filla,fillb,draina,drainb,a2b,b2a]
initial=[0,0]
visited=set()
stack=[(initial,[initial])]
while stack:
    state,path=stack.pop()
    if target in state:
        for i in path:
            print(str(i)+"-->",end="")
        if i[0]==target:
            print(str([target,0]))
        else:
            print(str([0,target]))
        break
    visited.add(tuple(state))
    for i in moves:
        x=i(state)
        if tuple(x) not in visited:
            new_path=path+[x]
            stack.append((x,new_path))
