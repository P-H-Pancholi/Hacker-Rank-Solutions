t = int(input())

for i in range(1,t+1):
	money, cost, n_wrappers_for_free_bar = map(int,input().split())
	chocolates_eaten = 0
	n_chocolates = money//cost
	chocolates_eaten += n_chocolates
	n_wrappers = n_chocolates
	print("chocolates_eaten ---- >",chocolates_eaten)
	while(n_wrappers >= n_wrappers_for_free_bar):
		n_chocolates = n_wrappers//n_wrappers_for_free_bar
		print("n_chocolates----- > ",n_chocolates)
		n_wrappers_left = n_wrappers%2
		chocolates_eaten += n_chocolates
		print("chocolates_eaten----- >", chocolates_eaten)
		n_wrappers = n_chocolates + n_wrappers_left
	print(chocolates_eaten)
