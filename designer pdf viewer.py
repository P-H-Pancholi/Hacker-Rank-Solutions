height_of_letters = raw_input()
height_of_letters = map(int,height_of_letters.split())


input_word = raw_input()
width = len(input_word)

input_word_list = []
for char in input_word:
    input_word_list.append(char)

get_individual_height = []
for letter in input_word_list:
    height = 0
    height = (height_of_letters[ord(letter)] - ord('a'))
    get_individual_height.append(height)

length = max(get_individual_height)

print(length*width)
