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
    print()


def func(s):
    function = [i / 2 for i in range(s)]
    graf = [[0 for i in range(s)] for j in range(s)]
    step = round((max(function) - min(function)) / s, 2)
    for i in range(s):
        graf[i][0] = round(step*(s-i), 2)
    for i in range(s):
        for j in range(s):
            if abs(function[j] - graf[i][0]) < step:
                if j != 0:
                    graf[i][j] = '!!'
            else:
                if j != 0:
                    graf[i][j] = '--'
         
    for i in graf:
        line = '\t' + str(float(i[0])) + '\t'
        for j in i[1:]:
            line += str(j)
        print(line)
    print('\t0\t', end='')
    for i in range(s):
        print(i, end=' ')




flag()
usor(2)
func(10)
