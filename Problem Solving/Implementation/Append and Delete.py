s = list(input())
t = list(input())
k = int(input())

if s == t:
	if k % 2 == 0 or k >= len(s)*2:
		print('Yes')
	else:
		print('No')
else:
	matchingChars = 0
	for i in range(0,min(len(s),len(t))):
		if s[i] != t[i]:
			break
		matchingChars += 1

	non_matching_chars_in_s = len(s) - matchingChars
	non_matching_chars_in_t = len(t) - matchingChars

	if (non_matching_chars_in_s + non_matching_chars_in_t) == k:
		result = 'Yes'
	elif (non_matching_chars_in_s + non_matching_chars_in_t < k) and (non_matching_chars_in_s + non_matching_chars_in_t - k) % 2 == 0):
		result ='Yes'
	elif (len(s) + len(t) <= k):
		result = 'Yes'
	else:
		result = 'No'
	print(result)
