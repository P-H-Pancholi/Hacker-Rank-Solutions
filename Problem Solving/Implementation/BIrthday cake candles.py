n = int(raw_input)
list_of_heights = raw_input()
list_of_heights = map(int,list_of_heights.split())
max_height = max(list_of_heights)
print list_of_heights.count(max_height)
