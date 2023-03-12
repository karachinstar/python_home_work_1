#-*- coding: cp1251 -*-   # без этой строки не хочет работать с кириллицей, можете объяснить почему?
usersec = int(input('Введите время в секундах: '))
print(f'Время в формате ч:м:с - {round(usersec / (60 * 60), 2)} : {round(usersec / (60), 2)} : {usersec}')
ch = usersec // (60 * 60)
m = (usersec - (ch * 60 * 60)) // 60
s = usersec - (ch * 60 * 60) - (m * 60)
print(f'Время в формате ч:м:с - {ch}:{m}:{s}')