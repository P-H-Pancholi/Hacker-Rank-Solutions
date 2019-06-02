money, cost, wrappers = map(int,input().split())
chocolates_eaten = 0
no_of_wrappers = 0

chocolates_eaten += money//cost
no_of_wrappers += chocolates_eaten

while(True):
	if no_of_wrappers >= wrappers:
		new_chocolates = no_of_wrappers//wrappers
		chocolates_eaten += new_chocolates
		no_of_wrappers = new_chocolates  + (no_of_wrappers % wrappers)
	else:
		break

print(chocolates_eaten)
