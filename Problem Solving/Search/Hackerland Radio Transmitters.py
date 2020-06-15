n, k = map(int,input().split())
loc_houses = list(map(int,input().split()))

loc_houses = sorted(loc_houses)

last = 0
i = 0
transmitter_req = 0

while i < n:
    transmitter = loc_houses[i]
    house = loc_houses[i]
    transmitter_req += 1

    while i < n and (loc_houses[i] - house) <= k:
        i += 1

    transmitter = i - 1

    while i < n and loc_houses[i] <= transmitter + k:
        i += 1


print(transmitter_req)
