str = input()
n = int(input())

a_in_substring = str.count('a')

n_of_such_substring = int(n/len(str))
n_remainder_of_substring = n%len(str)

temp_str = list(str)
remainder_of_substring = temp_str[0:n_remainder_of_substring]

a_in_remainder_of_substring = remainder_of_substring.count('a')

a_in_string = n_of_such_substring * a_in_substring + a_in_remainder_of_substring

print(a_in_string)
