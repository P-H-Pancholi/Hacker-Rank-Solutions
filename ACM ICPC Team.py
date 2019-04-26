n,m = map(int,input().split())

list_of_attendes = []
subjects_known_by_each_team = []


for attende in range(0,n):
    list_of_attendes.append(input())

for i in range(0,n-1):
    for j in range(i+1,n):
        subjects_known = int(list_of_attendes[i],2) | int(list_of_attendes[j],2)
        count_subjects_known = bin(subjects_known).count('1')
        subjects_known_by_each_team.append(count_subjects_known)

max_subject_known = max(subjects_known_by_each_team)
count_of_such_teams = subjects_known_by_each_team.count(max_subject_known)

print(max_subject_known)
print(count_of_such_teams)
