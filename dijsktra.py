from math import inf
from heapq import heapify,heappush
def dijkstra(graph,src,dest):
    node_data={}
    for key in graph:
        node_data[key]={'cost':inf,'pred':[]}
    node_data[src]['cost']=0
    temp=src
    visited=[]
    for i in range(len(graph)-1):
        if temp not in visited:
            visited.append(temp)
            min_heap=[]
            for j in graph[temp]:
                if j not in visited:
                    cost=node_data[temp]['cost']+graph[temp][j]
                    if cost<node_data[j]['cost']:
                       node_data[j]['cost']=cost
                       node_data[j]['pred']+=[temp]
                    heappush(min_heap,(node_data[j]['cost'],j))
            heapify(min_heap)
            temp=min_heap[0][1]
    print("Shortest Distance from",src,"to",dest,"is:",node_data[dest]['cost'])
    print("Shortest path is:",node_data[dest]['pred']+[dest])



op=1
while(op!=5):
    print("\n1.Add node\n2.Add Edge\n3.Finish\n4.Cancel\n5.Exit")
    op=int(input("Choose an option to perform: "))
    if(op==1):
        num=int(input("Enter the number of node: "))
        l=[]
        print("Enter the nodes: ")
        for i in range(num):
            l.append(input())
    elif(op==2):
        if(len(l)==0):
            print("\nNo node found")
        else:
            graph=dict()
            for i in range(len(l)):
                e=int(input("Enter the number of edges from node "+l[i]+":"))
                if e>0:
                    t=dict()
                    for j in range(e):
                        node=input("Enter the node:")
                        weight=int(input("Enter the weight from "+l[i]+" to "+node+" :"))
                        t[node]=weight
                graph[l[i]]=t
    elif(op==3):
        if(len(graph)==0):
            print("\nEmpty Graph")
        else:
            print("The graph obtained is:",graph)
            start=input("Enter the starting point: ")
            for dest in l:
                dijkstra(graph,start,dest)
    elif(op==4):
        l=[]
        graph=dict()
        print("\nGraph cleared")
    elif(op==5):
        print("\nThank You")
    else:
        print("\nInvalid Input")
