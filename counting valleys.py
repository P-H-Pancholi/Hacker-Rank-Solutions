n = int(input())
path = input()
path  = path.split()
valleys = 0
depth = 0
height = 0
for i in range(len(path)):
    print("FOR PATH",path[i])
    if path[i] == 'U':
        height+=1
        print("HEIGHT->",height)
    if path[i] == 'D':
        depht-=1
        print("DEPTH->",depth)
    if depth < 0 and path[i] == 'U':
        depth+=1
        print("DEPTH->",depth)
    if height > 0 and path[i] == 'D':
        height-=1
        print("HEIGHT->",height)
    if depth == 0:
        valleys+=1
print(valleys)
