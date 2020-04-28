m,n,r = map(int, input().split())
matrix = [input().split() for _ in range(m)]
no_of_layers = min(m,n)//2

for i in range(no_of_layers):
    rotations_required = r % ( 2 * ( m + n - 4 * i ) - 4)
    for rotation in range(rotations_required):

        #Rotate Top Row
        for j in range(i,n-i-1):
            matrix[i][j], matrix[i][j+1] = matrix[i][j+1], matrix[i][j]

        #Rotate Right column
        for j in range(i,m-i-1):
            matrix[j][n-i-1],matrix[j+1][n-i-1] = matrix[j+1][n-i-1], matrix[j][n-i-1]

		#Rotate Bottom Row
        for j in range(n-i-1,i,-1):
            matrix[m-i-1][j], matrix[m-i-1][j-1] = matrix[m-i-1][j-1], matrix[m-i-1][j]

        #Rotate Left Column
        for j in range(m-i-1,i+1,-1):
            matrix[j][i], matrix[j-1][i] = matrix[j-1][i], matrix[j][i]

for i in range(m):
    for j in range(n):
        print(matrix[i][j],end = " ")
        if j == n-1:
            print("\n",end="")
