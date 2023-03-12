#-*- coding: cp1251 -*-   # без этой строки не хочет работать с кириллицей, можете объяснить почему?
usernumber = str(input('Введите положительно число n: '))
print(f'{(usernumber)} + {usernumber + usernumber} + {usernumber + usernumber + usernumber} '
      f'= {int(usernumber) + int(str(usernumber + usernumber)) + int(str(usernumber + usernumber + usernumber)) }')