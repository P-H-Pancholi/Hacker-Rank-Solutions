t = int(input())
for i in range(0,t):
	b , w = map(int,input().split())
	bc, wc, z = map(int,input().split())

	total_cost = (b * bc) + (w * wc)

	if bc < wc:
		least_costly = bc
		adjusted_cost = (b + w) * least_costly + w * z
	else:
		least_costly = wc
		adjusted_cost = (b + w) * least_costly + b * z

	if adjusted_cost < total_cost:
		print(adjusted_cost)
	else:
		print(total_cost)
