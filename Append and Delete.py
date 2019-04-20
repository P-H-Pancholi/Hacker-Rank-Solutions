
def readchar(list,i=0):

	while i < len(list):
		char = list[i]
		i += 1
		return char

string1 = list('mukund')
string2 = list('mukund')

def get_cost(string1,string2):
	if len(string2) > len(string1):
		for i in range(0,len(string2)):
			if readchar(string1,i) != readchar(string2,i):
				for j in range(i,len(sring1)):
					string1.pop()
					print(string1)
				string1.append(string2[i])
	else:
		for k in range(len(string2),len(string1)):
			string1.pop()
		get_cost(string1,string2)

get_cost(string1,string2)

print(string1)
print(string2)
