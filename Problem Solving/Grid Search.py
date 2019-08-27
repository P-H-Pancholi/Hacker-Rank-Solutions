def gridSearch(G, P):
    patternFound = False
    #For each line of the grid:
    for a1 in range(0,len(G) - (len(P) - 1)):
        #For each column in give line:
        for a2 in range(0, len(G[a1]) - (len(P[0]) - 1)):
            #If the top left of the pattern matches the current value in the grid
            if P[0][0] == G[a1][a2]:
                #If the pattern fits horizontally in the matrix, try to match it
                if(len(P[0]) <= (len(G[a1]) - a2)):
                    #If the pattern 'fits' vertically in the matrix, try to match it
                    if(len(P) <= (len(G) - a1)):
                        #Match every single field of the pattern to the given area of the matrix.
                        for a3 in range(0,len(P)):
                            for a4 in range(0,len(P[0])):
                                #If the fields are equal patternFound is true
                                if(P[a3][a4] == G[a3+a1][a4+a2]):
                                    patternFound = True
                                else:
                                #If the fields are not equal stop matching this area of the matrix.
                                    patternFound = False
                                    break
                            #If one field in a line was not equal, stop matching this area of the matrix.
                            if(patternFound == False):
                                break
                    #If, after matching the whole area with the pattern patternFound is still true, the pattern is there.
                    if(patternFound):
                        break
        #If the pattern was found in the previous line, no need to keep this going.
        if(patternFound):
            break

    if(patternFound == True):
        return "YES"
    else:
        return "NO"






if __name__ == "__main__":
    t = int(input())
    for t_itr in range(t):
        RC = input().split()
        R = int(RC[0])
        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()
        r = int(rc[0])
        c = int(rc[1])

        P = []
        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)
        print(result)
