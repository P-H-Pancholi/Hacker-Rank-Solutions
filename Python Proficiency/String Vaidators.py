if __name__ == '__main__':
    s = input()
    isalnum = False
    isalpha = False
    isdigit = False
    islower = False
    isupper = False

    for char in s:
        if char.isalnum() == True:
            isalnum = True
        if char.isalpha() == True:
            isalpha = True
        if char.isdigit() == True:
            isdigit = True
        if char.isupper() == True:
            isupper = True
        if char.islower() == True:
            islower = True

    print(isalnum)
    print(isalpha)
    print(isdigit)
    print(islower)
    print(isupper)
