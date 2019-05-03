number_to_words = {
"00":"o' clock",
"01":"one","1":"one",
"02":"two","2":"two",
"03":"three","3":"three",
"04":"four","4":"four",
"05":"five","5":"five",
"06":"six","6":"six",
"07":"seven","7":"seven",
"08":"eight","8":"eight",
"09":"nine","9":"nine",
"10":"ten",
"11":"eleven",
"12":"twelve",
"13":"thirteen",
"14":"fourteen",
"15":"quater",
"16":"sixteen",
"17":"seventeen",
"18":"eighteen",
"19":"nineteen",
"20":"twenty",
"21":"twenty one",
"22":"twenty two",
"23":"twenty three",
"24":"twenty four",
"25":"twenty five",
"26":"twenty six",
"27":"twenty seven",
"28":"twenty eight",
"29":"twenty nine",
"30":"thirty",
}

hrs = input()
minutes = input()

if minutes == '00':
	print(number_to_words[hrs],number_to_words[minutes])
elif int(minutes) < 30:
	if minutes == '01':
		print(number_to_words[minutes],"minute past",number_to_words[hrs])
	elif minutes == '15':
		print(number_to_words[minutes],"past",number_to_words[hrs])
	else:
		print(number_to_words[minutes],"minutes past",number_to_words[hrs])
else:
	convert_minutes = str(60 - int(minutes))
	convert_hrs = str(int(hrs) + 1)
	if convert_minutes == '1':
		print(number_to_words[convert_minutes],"minute to",number_to_words[convert_hrs])
	elif convert_minutes == '15':
		print(number_to_words[convert_minutes],"to",number_to_words[convert_hrs])
	else:
		print(number_to_words[convert_minutes],"minutes to",number_to_words[convert_hrs])
