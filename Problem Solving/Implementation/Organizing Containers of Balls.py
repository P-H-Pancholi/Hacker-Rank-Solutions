t = int(input())

for _ in range(t):
    n = int(input())

    m = [list(map(int,input().split())) for _ in range(n)]

    #print(m)

    total_balls_in_container_i = [sum(row) for row in m]

    #print(total_balls_in_container_i)

    total_balls_of_value_i = []

    for j in range(n):
        balls_of_value_i = 0
        for i in range(n):
            balls_of_value_i += m[i][j]

        total_balls_of_value_i.append(balls_of_value_i)


    #print(total_balls_of_value_i)

    #We sort the values because the balls can be arranged in any containers...
    total_balls_of_value_i = sorted(total_balls_of_value_i)
    total_balls_in_container_i = sorted(total_balls_in_container_i)

    if total_balls_of_value_i == total_balls_in_container_i:
        print("Possible")
    else:
        print("Impossible")
