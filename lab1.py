def flag():
    for i in range(6):
        if i not in range(2,4):
            print('\x1b[48;5;231m        ',end=' ')
            print('\x1b[48;5;21m    ',end='')
            print('\x1b[48;5;231m        ',end=' ')
            print('\x1b[0;5;0m')
        else:
            print('\x1b[48;5;21m                      ',end='')
            print('\x1b[0;5;0m')
    print()


def step(mk, mark, end):
    print(f'{mk}',end='')
    print(f'\x1b[48;5;231m{mark}',end='')
    if end < -1:
        print(f'\x1b[0;5;0m{mk}', end = '')
    else:
        print(f'\x1b[0;5;0m{mk}')



def usor(kolvo):
    dlina = 12
    dlina_step = 10
    for i in range(1, 12):
        if i in range(4,9):
            mark = ' '*(2*dlina + 4)
            mk = ' '*2
            for st in range(kolvo):
                step(mk, mark, st-kolvo)
        elif i < 4:
            mark = ' '*(dlina+4*i)
            mk = ' '*(dlina_step-2*i)
            for st in range(kolvo):
                step(mk, mark, st-kolvo)
        else:
            mark = ' '*(dlina-4*(i-12))
            mk = ' '*(dlina_step+2*(i-12))
            for st in range(kolvo):
                step(mk, mark, st-kolvo)


def func():
    ...


flag()
usor(2)
