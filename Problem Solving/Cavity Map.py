def cavityMap(grid):
    #print(grid)
    for i in range(1,n-1):
        for j in range(1,n-1):
            value = grid[i][j]
            adjacent1 = grid[i-1][j]
            adjacent2 = grid[i+1][j]
            adjacent3 = grid[i][j-1]
            adjacent4 = grid[i][j+1]
            if value > adjacent1 and value > adjacent2 and value > adjacent3 and value > adjacent4:
                grid[i] = list(grid[i])
                grid[i][j] = 'X'
                grid[i] = "".join(grid[i])
    return grid




if __name__ == '__main__':
    n = int(input())
    grid = []
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)
    result = cavityMap(grid)
    print("\n")
    print("\n".join(result))
