n_k = input()
n_k = n_k.split()
n = int(n_k[0])
k = int(n_k[1])
arr = input()
arr = arr.split()
total = 0
count = 0 
for j in range(0,n):
    for i  in range(j+1,n):
        total = int(arr[j]) + int(arr[i])
        if total % k == 0:
            count = count +1
print(count)
