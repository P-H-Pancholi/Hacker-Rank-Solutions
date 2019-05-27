size = int(input())
pattern1 = ['-'*i for i in range(1,size*2)]
pattern2 = pattern1[-1::-1]
print("\n".join(pattern1),"\n".join(pattern2),sep = "")
