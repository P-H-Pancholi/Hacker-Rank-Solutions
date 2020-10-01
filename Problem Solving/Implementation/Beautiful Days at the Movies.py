input_i_j_k = raw_input()
input_i_j_k = map(int,input_i_j_k.split())
i = int(input_i_j_k[0])
j = int(input_i_j_k[1])
k = int(input_i_j_k[2])

count_beautiful_days = 0

for day in range(i,j+1):
    if ((abs(day - int(str(day)[::-1]))) % k) == 0:
        count_beautiful_days += 1

print count_beautiful_days
