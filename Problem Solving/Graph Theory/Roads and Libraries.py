class Node:

    def __init__(self,i):
        self.i = i;
        self.neighbouring_cities =  []

    def add_neighbouring_city(self,city):
        self.neighbouring_cities.append(city)


q = int(input())
for q in range(q):
    n_cities, m_roads, c_library, c_road = map(int,input().split())

    cities = [Node(i) for i in range(1,n_cities+1)]

    visited = [False for i in range(n_cities)]

    total_cost = 0



    for _ in range(m_roads):
        c1,c2 = map(int,input().split())
        cities[c1-1].add_neighbouring_city(cities[c2-1])
        cities[c2-1].add_neighbouring_city(cities[c1-1])


    #for j in range(n_cities):
    #    print(cities[j].i, cities[j].neighbouring_cities)

    if c_library <= c_road:
        total_cost = c_library*n_cities
        print(total_cost)
    else:

        for i,vis in enumerate(visited):
            cost_of_making_library = 0
            cost_of_making_road = 0
            if not vis:
                #print("IN ", i + 1, "Visit ")
                root = cities[i]
                queue = [root]
                total_cost += c_library
                cost_of_making_library += c_library

                while len(queue) > 0:
                    u = queue.pop(0)
                    #print("visited ", u.i)
                    visited[u.i -1 ] = True
                    nei_city = u.neighbouring_cities

                    for v in nei_city:
                        if visited[v.i -1] == False:
                            visited[v.i - 1] = True
                            queue.append(v)
                            total_cost += c_road
                            cost_of_making_road += c_road

            #print(visited)
        print(total_cost)
            #print("cost_of_making_road ", cost_of_making_road)
            #print("cost_of_making_library ", cost_of_making_library)
