# Переменная для определения очередности хода;
# 1 - первый игрок
# 2 - второй игрок
# 0 - игра заверешна.
hod = 1

# Матрица
A = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Фукнция для вывода матрицы, для удобного представления
def printm(M):
    for row in M:
        print(row)

# Возможные варианты для выигрыша
def fin(h,M):
    if   ((M[0][0] == h) and (M[0][1] == h) and (M[0][2] == h)) or \
            ((M[1][0] == h) and (M[1][1] == h) and (M[1][2] == h)) or \
            ((M[2][0] == h) and (M[2][1] == h) and (M[2][2] == h)) or \
            ((M[0][0] == h) and (M[1][0] == h) and (M[2][0] == h)) or \
            ((M[0][1] == h) and (M[1][1] == h) and (M[2][1] == h)) or \
            ((M[0][2] == h) and (M[1][2] == h) and (M[2][2] == h)) or \
            ((M[0][0] == h) and (M[1][1] == h) and (M[2][2] == h)) or \
            ((M[0][2] == h) and (M[1][1] == h) and (M[2][0] == h)):
        return True

# Функция для проверки "пустых" клеток в матрице
def checkm(M):
    for a in range(len(M)):
        for b in range(len(M[a])):
            if M[a][b] == 0:
                return True
    return False

#-----------------------------------------------------

# Вначале выводим матрицу
printm(A)

# Если есть пустые клетки и значение hod неравно 0
while (checkm(A) != False ) and (hod != 0):

    # Ход первого игрока
    if hod == 1:
        print('Ход 1 игрока')
        print('Введите координату x')
        x = input()
        print('Введите координату y')
        y = input()
        while  A[int(x)][int(y)] == 2 or A[int(x)][int(y)] == 1 :
            print('Клетка занята, походите ещё раз!')
            print('Введите координату x')
            x = input()
            print('Введите координату y')
            y = input()
        else:
            A[int(x)][int(y)] = 1
            # Проверка на выигрыш, если True, то заврешаем игру, иначе - передаём ход
            if fin(hod,A) == True:
                hod = 0
                print('Победил игрок 1')
            else:
                hod = 2
        printm(A)

    # Ход второго игрока
    elif hod == 2:
        print('Ход 2 игрока')
        print('Введите координату x')
        x = input()
        print('Введите координату y')
        y = input()
        while  A[int(x)][int(y)] == 2 or A[int(x)][int(y)] == 1 :
            print('Клетка занята, походите ещё раз!')
            print('Введите координату x')
            x = input()
            print('Введите координату y')
            y = input()
        else:
            A[int(x)][int(y)] = 2
            if fin(hod, A) == True:
                hod = 0
                print('Победил игрок 2')
            else:
                hod = 1
        printm(A)

    else:
        None

else:
    print('Игра завершена')