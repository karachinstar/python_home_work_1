#-*- coding: cp1251 -*-   # без этой строки не хочет работать с кириллицей, можете объяснить почему?
username = input('Введите имя: ')
userpassword = input('Введите ваш пароль: ')
userage = int(input('Введите ваш возраст: '))
print(f'Ваше имя - "{username}", пароль - "{userpassword}", возраст - "{userage}"')