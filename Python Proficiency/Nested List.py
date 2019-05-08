n = int(input())
nested_list = []

def getscore(element):
	return element[1]

for student in range(n):
	temp = []
	name = input()
	score = float(input())
	temp.append(name)
	temp.append(score)
	nested_list.append(temp)

nested_list.sort(key = getscore)
min_score = nested_list[0][1]
second_min_score = 0

for student in nested_list:
	if student[1] > min_score:
		second_min_score = student[1]
		break

students = [student for student in nested_list if student[1] == second_min_score]
students.sort()

for student in students:
	print(student)
