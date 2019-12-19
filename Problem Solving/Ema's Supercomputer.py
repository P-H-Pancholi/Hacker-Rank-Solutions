n,m = map(int,input().split())
grid = []
for _ in range(n):
    grid.append(list(str(input().strip())))

#print(grid)
max1 = 0
max1_i = 0
max1_j = 0
max2 = 0
max2_i = 0
max2_j = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == 'G':
            for k in range(min(n,m)):
                if i + k < n and i - k >= 0 and j + k < m and j - k >= 0 :
                    #print("Checking for i,j,k ",i,j,k,sep=" ,")
                    if grid[i+k][j] == 'G' and grid[i-k][j] == 'G' and grid[i][j+k] == 'G' and grid[i][j-k] == 'G':
                        if k+1 >= max1:
                            max1 = k+1
                            max1_i = i
                            max1_j = j
                    else:
                        break

#print("MAX1, i,j",max1,max1_i,max1_j,sep = "---")


for k in range(max1):
    grid[max1_i + k][max1_j] = 'B'
    grid[max1_i - k][max1_j] = 'B'
    grid[max1_i][max1_j + k] = 'B'
    grid[max1_i][max1_j - k] = 'B'

#print(grid)
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'G':
            for k in range(min(n,m)):
                if i + k < n and i - k >= 0 and j + k < m and j - k >= 0 :
                    #print("Checking for i,j,k ",i,j,k,sep=" ,")
                    if grid[i+k][j] == 'G' and grid[i-k][j] == 'G' and grid[i][j+k] == 'G' and grid[i][j-k] == 'G':
                        if k+1 >= max2:
                            max2 = k+1
                            max2_i = i
                            max2_j = j
                    else:
                        break


#print("MAX2, i,j",max2,max2_i,max2_j,sep = "---")
area = (max1 * 4 - 3) * (max2 * 4 - 3)
print(area)
