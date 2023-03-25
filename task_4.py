revenue = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))
if revenue > costs:
    print(f'Финансовый результат - прибыль. Ее величина: {revenue - costs}')
    print(f'Рентабельность выручки = {costs / revenue}')
    number_of_staff = int(input('Введите численность сотрудников: '))
    print(f'Прибыль фирмы в расчете на одного сотрудника '
          f'=  {(revenue - costs) / number_of_staff}')
else:
    print(f'Финансовый результат - убыток. Его величина: {costs - revenue}')