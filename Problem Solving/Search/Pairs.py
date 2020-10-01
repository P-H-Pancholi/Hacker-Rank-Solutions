n,k = map(int, input().split())
n_list = sorted(list(map(int, input().split())))
set_n_list = set(n_list)

pairs_count = 0

for v in set_n_list:
    if v+k in set_n_list:
        pairs_count += 1

print(pairs_count)
