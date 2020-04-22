
t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int,input().split()))


    solution_matrix = [[0,0] for i in range(n)]

    for i in range(1,n):
        solution_matrix[i][1] = max(solution_matrix[i-1][0] + (abs(b[i] - 1)), solution_matrix[i-1][1] + (abs(b[i-1] - b[i])))
        solution_matrix[i][0] = max(solution_matrix[i-1][1] + abs(1 - b[i-1]), solution_matrix[i-1][0] + abs((1 - 1)))

    print(max(solution_matrix[n-1][0],solution_matrix[n-1][1]))
