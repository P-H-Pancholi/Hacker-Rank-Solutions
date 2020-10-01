n_test_cases = int(raw_input())

data_list = []

for i in range(n_test_cases):
    test = []
    n_m_s = raw_input()
    n_m_s = map(int,n_m_s.split())
    number_of_prisoners = n_m_s[0]
    number_of_candies = n_m_s[1]
    starting_chair = n_m_s[2]
    test.append(number_of_prisoners)
    test.append(number_of_candies)
    test.append(starting_chair)
    data_list.append(test)

def prisoner(number_of_prisoners, candy, current_prisoner):
    candy %= number_of_prisoners
    current_prisoner += candy - 2
    return 1 + (current_prisoner % number_of_prisoners)


for test in data_list:
    current_prisoner = test[2]
    candy = test[1]
    number_of_prisoner = test[0]
    print prisoner(number_of_prisoner,candy,prisoner)
