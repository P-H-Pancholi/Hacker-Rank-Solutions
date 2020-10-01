h, w = map(int,input().split())
matrix0 = [list(map(int,input().split())) for _ in range(h)]

#print(matrix)

bottom_and_top_surface_area = 2 * h * w

surface_area = 2 * h * w
front_back_surface_area = 0

for row in matrix0:
	print(row)
	front_back_surface_area += row[0] + row[w-1] + sum([abs(row[i] - row[i+1]) for i in range(0,w-1)])
	print(front_back_surface_area)
print(front_back_surface_area)

matrix1 = []

for j in range(w):
	temp = [matrix0[i][j] for i in range(h)]
	matrix1.append(temp)



left_right_surface_area = 0

for row in matrix1:
	print(row)
	left_right_surface_area += row[0] + row[h-1] + sum([abs(row[i] - row[i+1]) for i in range(0,h-1)])
	print(left_right_surface_area)
print(left_right_surface_area)

total_surface_area = bottom_and_top_surface_area + front_back_surface_area + left_right_surface_area
print(total_surface_area)
