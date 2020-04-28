class Astronaut:

    def __init__(self,id):
        self.id = id;
        self.astronaut_belonging_to_same_country =  []

    def add_fellow_astronaut(self,astornaut):
        self.astronaut_belonging_to_same_country.append(astornaut)



n , p = map(int,input().split())

astronauts = [Astronaut(i) for i in range(0,n)]

astronauts_in_each_country = []

for _ in range(p):
    a1,a2 = map(int,input().split())
    astronauts[a1].add_fellow_astronaut(astronauts[a2])
    astronauts[a2].add_fellow_astronaut(astronauts[a1])


visited = [False for _ in range(n)]

for i,vis in enumerate(visited):
    if not vis:
        n_fellow_citizens = 1
        root = astronauts[i]
        queue = [root]

        while len(queue) > 0:
            u = queue.pop(0)
            #print("visited ", u.i)
            visited[u.id] = True
            fellow_citizens = u.astronaut_belonging_to_same_country

            for v in fellow_citizens:
                if visited[v.id] == False:
                    visited[v.id] = True
                    n_fellow_citizens += 1
                    queue.append(v)

        #print(n_fellow_citizens)
        astronauts_in_each_country.append(n_fellow_citizens)


total_combinations = 0

for i in range(0,len(astronauts_in_each_country)-1):
    for j in range(1+i,len(astronauts_in_each_country)):
        total_combinations += astronauts_in_each_country[i] * astronauts_in_each_country[j]

print(total_combinations)
