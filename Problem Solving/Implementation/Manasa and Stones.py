def stones(n, a, b):
    end = []
    for i in range(n):
        end.append(((n-1) - i)*b + (i*a))
    end = sorted(set(end))
    end = map(str,end)
    return end

if __name__ == "__main__":
    T = int(input())
    for T_itr in range(T):
        n = int(input())
        a = int(input())
        b = int(input())
        result = stones(n, a, b)
        print(" ".join(result))
