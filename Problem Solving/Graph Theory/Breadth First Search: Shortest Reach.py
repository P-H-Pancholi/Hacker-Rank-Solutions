class Node:

    def __init__(self,i):
        self.i = i
        self.adj = []

    def add_edge(self,adj_node):
        self.adj.append(adj_node)



q = int(input())

for _ in range(q):
    n , m = map(int, input().split())

    nodes = [Node(i) for i in range(1,n+1)]

    for i in range(m):
        n1,n2 = map(int,input().split())
        nodes[n1-1].add_edge(nodes[n2-1])
        nodes[n2-1].add_edge(nodes[n1-1])

    root = nodes[int(input()) - 1]

    visited = [0 for _ in range(n)]
    idx = 1

    queue = [root]

    while len(queue) > 0:
        u = queue.pop(0)
        if visited[u.i - 1] <= 0:
            visited[u.i - 1] = -1
        adj_u = u.adj

        for v in adj_u:
            if visited[v.i -1] == 0:
                visited[v.i -1] = idx
                queue.append(v)

        print(visited)

    for i in range(0,n):
        if visited[i] == -1:
            continue

        if visited[i] == 0:
            print("-1",end = " ")
        else:
            print(6*visited[i],end = " ")

    print()
