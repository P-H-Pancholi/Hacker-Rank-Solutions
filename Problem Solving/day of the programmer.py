year = int(input())
if year in range(1700,1918):
    if year % 4 == 0:
        print('12.09.',year,sep="")
    else:
        print('13.09.',year,sep="")
if year in range(1919,2701):
    if year % 4 == 0 and year % 100 != 0:
        print('12.09.',year,sep="")
    elif year % 400 == 0:
        print('12.09.',year,sep="")
    else:
        print('13.09.',year,sep="")
if year == 1918:
    print('26.09.1918')
