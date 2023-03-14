usernumber = int(input('Введите трехзначное число: '))
if usernumber >= 1000 or usernumber <= 100:
    print(f'Вы ввели не трехзначное число')
else:
    print(f'Сумма  цифр трехзначного числа {usernumber} = '
          f'{(usernumber // 100) + (usernumber % 10) + ((usernumber // 10) % 10)}')