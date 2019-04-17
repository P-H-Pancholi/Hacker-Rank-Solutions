n_k = raw_input()
n_k = map(int,n_k.split())
n = n_k[0]#number of hurdles
k = n_k[1]#max height dan can jump
height_of_hurdles = raw_input()
height_of_hurdles = map(int,height_of_hurdles.split())

if k < max(height_of_hurdles):
    print(max(height_of_hurdles) - k)
else
    print(0)
