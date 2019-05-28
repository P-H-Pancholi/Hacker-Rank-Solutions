p, d, m, s = map(int,input().split())
count = 0
while(True):
	if s < p:
		break
		
	print(p,end = " ")
	count += 1
	s -= p
	p -= d
	if p <= m:
		p = m


print(count)
