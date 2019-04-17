t = int(raw_input())

list_of_n = [] #number of students
list_of_k = [] #threshold time
list_of_times = []

for i in range(t):
    n_k = raw_input()
    n_k = map(int,n_k.split())
    n = n_k[0]
    list_of_n.append(n)
    k = n_k[1]
    list_of_k.append(k)
    time_by_student = raw_input()
    time_by_student = map(int,time_by_student.split())
    list_of_times.append(time_by_student)

for test in range(t):
    early_students = 0
    for student_time in list_of_times[test]:
        if student_time <= 0:
            early_students += 1
    if early_students >= list_of_k[test]:
        print "NO"
    else:
        print "YES"
