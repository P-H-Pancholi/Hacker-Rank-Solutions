n,m,k = map(int,input().split())
n_lamps = n*m

map_dict = dict()

for i in range(1,n+1):
    map_dict[i] = []

for _ in range(k):
    r,c1,c2 =  map(int,input().split())
    map_dict[r].append([c1, c2])

for row in map_dict:
    intervals = sorted(map_dict[row], reverse=True)
    n = len(intervals)
    cursor = 0
    for i in range(0, n):
        if (cursor != 0 and intervals[i][1] >= intervals[cursor-1][0]):
            while (cursor != 0 and intervals[i][1] >= intervals[cursor-1][0]):
                # While current interval overlaps with previous interval --> Merge
                intervals[cursor-1][0] = min(intervals[cursor-1][0], intervals[i][0])
                intervals[cursor-1][1] = max(intervals[cursor-1][1], intervals[i][1])
                cursor -= 1
        else:
            intervals[cursor] = intervals[i]

        cursor += 1

    map_dict[row] = intervals[:cursor]

for row in map_dict:
    intervals = map_dict[row]
    ans = 0
    for interval in intervals:
        ans += interval[1] - interval[0] + 1

    n_lamps -= ans

print(n_lamps)
