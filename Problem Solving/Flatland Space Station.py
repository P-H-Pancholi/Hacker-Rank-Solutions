n, m = map(int,input().split())
list_of_indices = list(map(int,input().split()))
cities = [city for city in range(n) if city not in list_of_indices]
maximum = 0

for city in cities:
    diff_city_space = [abs(city - list_of_indices[i]) for i in range(m)]
    minimum = min(diff_city_space)
    if minimum > maximum:
        maximum = minimum



if maximum:
    print(maximum)
else:
    print("0")
