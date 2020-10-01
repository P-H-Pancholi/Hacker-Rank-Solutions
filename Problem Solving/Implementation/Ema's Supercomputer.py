from copy import deepcopy
n,m = map(int,input().split())
MAT = [list(input()) for _ in range(n)]
MAT1 = MAT

def print_matrix(MAT1):
    print("MATRIX")

    for row in MAT1:
        print("".join(row))


def check_plus(i,j,n,m,MAT1):
    cells_above = 0
    cells_below = 0
    cells_right = 0
    cells_left = 0

    #Cells above (i,j)
    k = i
    while k >= 0 and MAT1[k][j] == 'G':
        cells_above += 1
        k -= 1

    #Cells below (i,j)
    k = i
    while k < n and MAT1[k][j] == 'G':
        cells_below += 1
        k += 1

    #Cells right (i,j)
    l = j
    while l >= 0 and MAT1[i][l] == 'G':
        cells_left += 1
        l -= 1

    #Cells left (i,j)
    l = j
    while l < m and MAT1[i][l] == 'G':
        cells_right += 1
        l += 1

    max_plus = min(cells_left,cells_above,cells_below,cells_right)
    print(max_plus)

    return max_plus + 3 * (max_plus - 1)

res1 = []
res12 = []
size1 = 0

for i in range(n):
    for j in range(m):
        if MAT1[i][j] == 'B':
            continue
        res = check_plus(i,j,n,m,MAT)
        if res > size1:
            row,col = i,j
            size1 = res
            res1.append((res,i,j))


print(res1)

#generate other results:

for result in res1:
    max_res = result[0]
    res12.append(result)

    max_res -= 4
    while max_res > 0:
        res12.append((max_res, result[1], result[2]))
        max_res -= 4


print(res12)

final_result = []

MAT2 = deepcopy(MAT)
for result in res12:
    res2 = []
    size1 = result[0]
    print("FOR RESULT ", result)
    cells_to_color = (result[0] + 3)//4
    row,col = result[1],result[2]

    print_matrix(MAT2)

    for cell in range(cells_to_color):
        MAT2[row + cell][col] = 'B'
        MAT2[row - cell][col] = 'B'
        MAT2[row][col + cell] = 'B'
        MAT2[row][col - cell] = 'B'

    print_matrix(MAT2)

    size2 = 0
    row,col = 0,0

    for i in range(n):
        for j in range(m):
            if MAT2[i][j] == 'B':
                continue
            res = check_plus(i,j,n,m,MAT1)
            res2.append(res)
    print(res2)
    MAT2 = deepcopy(MAT)
