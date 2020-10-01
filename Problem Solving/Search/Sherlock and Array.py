t = int(input())

for _ in range(t):
    n = int(input())
    n_list = list(map(int, input().split()))

    sum_right = sum(n_list)
    sum_left = 0

    for i in range(n):

        if i == 0:
            sum_right = abs(sum_right - n_list[i])
        else:
            sum_left += n_list[i-1]
            sum_right = abs(sum_right - n_list[i])

        #print("sum_left = {}   sum_right = {}".format(sum_left, sum_right))

        if sum_left == sum_right:
            print("YES")
            break
    else:
        print("NO")
