ticket_n = int(input('Введите номер билета: '))
if len(str(ticket_n)) % 2 == 0:
    sum_1 = 0
    sum_2 = 0
    ticket_n_1 = ticket_n // 10 ** ((len(str(ticket_n))) / 2)
    ticket_n_2 = ticket_n % 10 ** ((len(str(ticket_n))) / 2)
    while (ticket_n_1 != 0) and (ticket_n_2 != 0):
        sum_1 = sum_1 + (ticket_n_1 % 10)
        ticket_n_1 = ticket_n_1 // 10
        sum_2 = sum_2 + (ticket_n_2 % 10)
        ticket_n_2 = ticket_n_2 // 10
    if sum_1 == sum_2:
        print(f'Билет № {ticket_n} - счастливый')
    else:
        print(f'Билет № {ticket_n} - несчастливый')
else:
    print(f'Билет № {ticket_n} - несчастливый')