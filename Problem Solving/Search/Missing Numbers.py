n = int(input())
n_list = sorted(list(map(int, input().split())))
m = int(input())
m_list = sorted(list(map(int, input().split())))

n_count = [0 for _ in range(101)]
m_count = [0 for _ in range(101)]

offset = min(m_list)

for num in n_list:
    n_count[num - offset] += 1

for num in m_list:
    m_count[num - offset] += 1

for i in range(101):
    if n_count[i] != m_count[i]:
        print(offset + i)
