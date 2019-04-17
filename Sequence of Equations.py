n = int(raw_input())
list_of_numbers = raw_input()
list_of_numbers = map(int,list_of_numbers.split())
dict = {}
index = 1
for number in list_of_numbers:
    dict.update({number:index})
    index += 1

for x in range(1,n+1):
    y = dict[dict[x]]
    print y
