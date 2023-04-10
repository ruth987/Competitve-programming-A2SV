from collections import defaultdict

n  = int(input())
k = int(input())
graph = defaultdict(list)

def addEdge(v, u):
    graph[v].append(u)
    graph[u].append(v)


def vertex(v):
    print(*graph[v])

for _ in range(n):
    arr = list(map(int, input().split()))

    if arr[0] == 1:
        addEdge(arr[1], arr[2])
    
    else: # arr[0] == 2
        vertex(arr[1])
