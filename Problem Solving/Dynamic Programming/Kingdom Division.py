class Node:

    def __init__(self,i):
        self.i = i
        self.neighbours = []


    def add_edge(self,neighbour):
        self.neighbours.append(neighbour)

    def get_neighbour_len(self)
        return len(self.neighbours)


def dfs(n,v,visited):

    print(v.i)

    if all(visited):
            return 0
    else:
        for neighbour in v.neighbours:
            #print(neighbour.i)
            visited[neighbour.i - 1] = True

            dfs(n,neighbour,visited)














if __name__ == "__main__":
    n = 6

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)

    n1.add_edge(n2)
    n1.add_edge(n3)
    n1.add_edge(n6)

    n3.add_edge(n4)
    n3.add_edge(n5)

    #print(n2.neighbours)

    visited = [False for _ in range(n)]

    dfs(n,n1,visited)
