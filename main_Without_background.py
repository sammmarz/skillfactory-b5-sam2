field = [
    ['*', '*', '*'],
    ['*', '*', '*'],
    ['*', '*', '*']
]


def show_field(f):
    print('  0 1 2 ')
    for i in range(len(f)):
        print(str(i), *f[i])

def user_input(f,player):

    while True:
        coor_xy = input(f'Введите координаты для  {player}  ').split()
        if len(coor_xy)!=2:
            print('Введено более 2 координат. Повторите ввод')
            continue
        if not(all(str(x).isdigit() for x in coor_xy)):
            print('Введите числа')
            continue
        x,y = map(int, coor_xy)
        if not(x >= 0 and x < 3 and y >= 0 and y < 3):
            print("Введите 2 числа в диапазоне 0-2")
            continue
        if f[x][y] != '*':
            print('Поле занято. Повторите ввод координат')
            continue
        break
    return x,y
def check_win(f,user):
    def check_line(mas1, mas2, mas3, user):
        if mas1 == user and mas2 == user and mas3 == user:
            return True;
    for i in range(len(f)):
        if check_line(f[i][0], f[i][1],f[i][2], user) or \
           check_line(f[0][i], f[1][i], f[2][i], user) or \
           check_line(f[0][0], f[1][1], f[2][2], user) or \
           check_line(f[0][2], f[1][1], f[2][0], user):
            return True
    return False;

count = 0
show_field(field)
while 1:
    if count % 2:
        user = '0'
    else:
        user = 'x'
    x,y = user_input(field, user)
    field[x][y] = user
    show_field(field)
    if check_win(field, user):
        print(f"Выиграл {user}")
        break
    if count == 9:
        print("Ничья")
        break
    count += 1

