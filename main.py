import random as rn

n = rn.randint(4, 30)
hod = 1
k = 0

while True:
    if hod == 1:
        while k <= 0 or k > 3:
            print('----------\n'
                  'Ход игрока 1\n'
                  f'Осталось {n} камней\n'
                  'Введите число от 1 до 3:')
            try:
                k = int(input())
            except ValueError:
                print('!!!Ошибка ввода!!!')
            else:
                if k <= 0 or k > 3:
                    print('!Введено не верное число!')
        n -= k
        k = 0
        if n <= 0:
            print('\nИгрок 2 выиграл')
            break
        hod = 1
    elif hod == 2:
        while k <= 0 or k > 3:
            print('----------\n'
                  'Ход игрока 2\n'
                  f'Осталось {n} камней\n'
                  'Введите число от 1 до 3:')
            try:
                k = int(input())
            except ValueError:
                print('!!!Ошибка ввода!!!')
            else:
                if k <= 0 or k > 3:
                    print('!Введено не верное число!')
        n -= k
        k = 0
        if n <= 0:
            print('\nИгрок 1 выиграл')
            break
        hod = 1
