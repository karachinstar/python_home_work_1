#-*- coding: cp1251 -*-   # ��� ���� ������ �� ����� �������� � ����������, ������ ��������� ������?
usersec = int(input('������� ����� � ��������: '))
print(f'����� � ������� �:�:� - {round(usersec / (60 * 60), 2)} : {round(usersec / (60), 2)} : {usersec}')
ch = usersec // (60 * 60)
m = (usersec - (ch * 60 * 60)) // 60
s = usersec - (ch * 60 * 60) - (m * 60)
print(f'����� � ������� �:�:� - {ch}:{m}:{s}')