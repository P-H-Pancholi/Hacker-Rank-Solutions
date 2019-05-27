def print_formatted(number):
	for i in range(1,n+1):
		binary = bin(i)[2:]
		padding = len(bin(number)[2:])
		binary = int(binary)
		print("%*d %*o %*X %*d" %(padding,i,padding,i,padding,i,padding,binary))



if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
