from math import inf
def alphabeta(depth,values,node,alpha,beta,is_maximizing):
    if depth==max_depth:
        return values[node]
    if is_maximizing:
        value=alpha
        for i in range(2):
            score=alphabeta(depth+1,values,node*2+i,alpha,beta,False)
            value=max(value,score)
            alpha=max(alpha,value)
            print("\nLevel: ",depth)
            print("alpha: ",alpha)
            print("beta: ",beta)
            if alpha>=beta:
                print("Pruning Done")
                break
        return value
    else:
        value=beta
        for i in range(2):
            score=alphabeta(depth+1,values,node*2+i,alpha,beta,True)
            value=min(score,value)
            beta=min(beta,value)
            print("\nLevel: ",depth)
            print("alpha: ",alpha)
            print("beta: ",beta)
            if alpha>=beta:
                print("Pruning Done")
                break
        return value

alpha=-inf
beta=inf
values=[]
max_depth=int(input("Enter the depth of the tree: "))
for i in range(2**max_depth):
    values.append(int(input("Enter the value "+str(i+1)+" : ")))
print("The Optimal Value is: ",alphabeta(0,values,0,alpha,beta,True))
