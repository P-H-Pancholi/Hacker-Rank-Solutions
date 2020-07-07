
class Position:

    def __init__(self,x,y,steps_taken):
        self.x = x
        self.y = y
        self.steps_taken = steps_taken


def check_in_board(x,y,n):
    if x >= 0 and x <= n-1  and y >= 0 and y <= n-1:
        return True

    return False



def get_min_steps(n,i,j):

    jump_x = [i,i,j,j,-i,-i,-j,-j]
    jump_y = [j,-j,i,-i,j,-j,i,-i]

    #print("[INFO] i = {} j = {}".format(i,j))

    #print(jump_x)
    #print(jump_y)

    visited = [[False for _ in range(n)] for _ in range(n)  ]

    start = Position(0,0,0)

    queue = [start]

    while len(queue) > 0:

        pos = queue.pop(0)
        visited[pos.x][pos.y] = True
        steps_taken = pos.steps_taken
        #print(pos.x,pos.y)

        if pos.x == n-1 and pos.y == n-1:
            return steps_taken

        for i in range(8):
            new_pos_x = pos.x + jump_x[i]
            new_pos_y = pos.y + jump_y[i]
            if check_in_board(new_pos_x, new_pos_y, n):
                #print(new_pos_x, new_pos_y, visited[new_pos_x][new_pos_y], check_in_board(new_pos_x, new_pos_y, n))
                if not visited[new_pos_x][new_pos_y]:
                    queue.append(Position(new_pos_x, new_pos_y, steps_taken+1))
                    visited[new_pos_x][new_pos_y] = True
                    #print(queue)

    return -1


if __name__ == "__main__":
    n = int(input())

    solution_matrix = [ [0 for _ in range(n-1)] for _ in range(n-1)]


    for i in range(1,n):
        for j in range(i,n):
            min_steps = get_min_steps(n,i,j)
            solution_matrix[i-1][j-1] = str(min_steps)
            solution_matrix[j-1][i-1] = str(min_steps)

    for row in solution_matrix:
        print(" ".join(row))
