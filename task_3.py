#-*- coding: cp1251 -*-   # ��� ���� ������ �� ����� �������� � ����������, ������ ��������� ������?
usernumber = str(input('������� ������������ ����� n: '))
print(f'{(usernumber)} + {usernumber + usernumber} + {usernumber + usernumber + usernumber} '
      f'= {int(usernumber) + int(str(usernumber + usernumber)) + int(str(usernumber + usernumber + usernumber)) }')