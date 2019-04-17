q =  int(input())
queries = []
for i in range(0,q):
    query = input()
    queries.append(query)

for x in queries:
    x = x.split()
    PA = int(x[0])
    PB = int(x[1])
    PC = int(x[2])
    if abs(PC - PA) > abs(PB - PC):
        print("Cat B")
    elif abs(PC - PA) < abs(PB - PC):
        print("Cat A")
    else:
        print("Mouse C")
