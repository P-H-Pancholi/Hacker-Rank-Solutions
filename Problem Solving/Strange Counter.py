def getValue(t):
    return 6 * math.pow(2, math.floor(math.log2((t+2)/3))) - 2 - t

t = in(input())
getValue(t)
