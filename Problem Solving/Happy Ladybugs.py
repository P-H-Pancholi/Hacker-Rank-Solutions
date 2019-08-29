from collections import Counter
def happyLadybugs(b):
    counter = Counter(b)
    for key, value in counter.items():
        if key != "_" and value == 1:
            return "NO"

    if "_" in b:
        return "YES"

    for idx in range(1, len(b)):
        if b[idx] == b[idx-1] or b[idx] == b[idx+1]:
            continue
        else:
            return "NO"

    return "YES"







if __name__ == "__main__":
    g = int(input())
    result = []
    for g_itr in range(g):
        n = int(input())
        b = input()
        result.append(happyLadybugs(b))
    print("\n".join(result))
