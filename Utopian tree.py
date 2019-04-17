t = int(raw_input())
list_of_cycles = []

for i in range(t):
    n = int(raw_input())
    list_of_cycles.append(n)

height  = 0

def get_height_after_period(period):
    global height
    if period == 0:
        height = 1
    elif period % 2 == 0:
        height = 1 + get_height_after_period(period - 1)
    else:
        height = 2 * get_height_after_period(period - 1)
    print height

for period in list_of_cycles:
    get_height_after_period(period)
