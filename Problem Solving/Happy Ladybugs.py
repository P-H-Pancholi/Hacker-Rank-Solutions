def happyLadybugs(b):
    bSet = set(b)
    for bug in bSet:
        countbug = 0
        countempty = 0
        for checkbug in b:
            if checkbug == "_":
                countempty += 1
                continue
            if checkbug == bug:
                countbug += 1
            print(countbug)
        if countbug == 1:
            return "NO"
    if countempty:
        return "YES"
    else:
        return "NO"




if __name__ == "__main__":
    g = int(input())
    result = []
    for g_itr in range(g):
        n = int(input())
        b = input()
        result.append(happyLadybugs(b))
    print("\n".join(result))
