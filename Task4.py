#num_hours1 = int(input('Enter num_hours1 '))
#num_min1 = int(input('Enter num_min1 '))
#num_sec1 = int(input('Enter num_sec1 '))
#num_hours2 = int(input('Enter num_hours2 '))
#num_min2 = int(input('Enter num_min2 '))
#num_sec2 = int(input('Enter num_sec2 '))
#print('Result: ')
#print(((num_hours2-num_hours1)*3600)+((num_min2-num_min1)*60)+(num_sec2-#num_sec1))


point1 = input('Введите часы, минуты и секунды через пробел: ').split()
h = int(point1[0])*60*60
m = int(point1[1])*60
s = int(point1[2])
seconds_point1 = h + m + s
point2 = input('Введите часы, минуты и секунды через пробел: ').split()
h2 = int(point2[0])*60*60
m2 = int(point2[1])*60
s2 = int(point2[2])
seconds_point2 = h2 + m2 + s2
all_seconds = seconds_point1 - seconds_point2
result = abs(all_seconds)
print('Результат: ' + str(result) + ' cекунд.')
