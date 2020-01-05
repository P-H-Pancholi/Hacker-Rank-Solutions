abc = "abcdefghijklmnopqrstuvwxyz"
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(inp, k):
    out = ["*" for i in range(len(inp))]
    for i in range(len(inp)):
        if inp[i] in abc:
            enc_ind = ((abc.index(inp[i]) + k) % 26)
            out[i] = abc[enc_ind]
            #print(out)
        elif inp[i] in ABC:
            enc_ind = ((ABC.index(inp[i]) + k) % 26) -1
            enc_ind = ((ABC.index(inp[i]) + k) % 26)
            out[i] = ABC[enc_ind]
            #print(out)
        else:
            out[i] = inp[i]
    return out




n = int(input())
inp = input().rstrip()
k = int(input())

out = encrypt(inp, k)

print("".join(out))
