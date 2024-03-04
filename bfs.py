def bfs(graph,node):
    visited=[]
    queue=[]
    visited.append(node)
    queue.append(node)
    while queue:
        q=queue.pop(0)
        print(q,end=" ")
        for i in graph[q]:
            if i not in visited:
                visited.append(i)
                queue.append(i)



op=1
while(op!=5):
    print("\n1.Add Vertex\n2.Add Edge\n3.Finish\n4.Cancel\n5.Exit")
    op=int(input("Choose an option to perform: "))
    if(op==1):
        num=int(input("Enter the number of vertex: "))
        l=[]
        print("Enter the vertices: ")
        for i in range(num):
            l.append(int(input()))
    elif(op==2):
        if(len(l)==0):
            print("\nNo vertex found")
        else:
            graph=dict()
            for i in range(len(l)):
                e=int(input("Enter the number of edges from vertex "+str(l[i])+":"))
                if e>0:
                    print("Enter the vertex of the edges one by one:")
                t=[]
                for j in range(e):
                    t.append(int(input()))
                graph[l[i]]=t
    elif(op==3):
        if(len(graph)==0):
            print("\nEmpty Graph")
        else:
            print("The graph obtained is:",graph)
            start=int(input("Enter the starting point: "))
            print("The result obtained after performing DFS is: ",end="")
            bfs(graph,start)
    elif(op==4):
        l=[]
        graph=dict()
        print("\nGraph cleared")
    elif(op==5):
        print("\nThank You")
    else:
        print("\nInvalid Input")
