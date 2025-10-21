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
    print()

    
def diag():
    with open('sequence.txt') as sequence:
        ls = [float(i) for i in sequence]
        ls1 = [float(i) for i in ls if -10 < float(i) < -5]
        ls2 = [float(i) for i in ls if 10 > float(i) > 5]
        lproc1 = round(len(ls1) / (len(ls1)+len(ls2)) * 100, 2)
        lproc2 = 100 - lproc1
        line1 = ' '*int(lproc1)
        line2 = ' '*int(lproc2)
        print('\t' + ' '*49 + '|')
        for i in range(2):
            print('\t' + f'\x1b[48;5;231m{line1}' + f'\x1b[48;5;21m{line2}' + '\x1b[0;5;0m')
        print('\t' + ' '*49 + '|')
        print(' '*20 ,'-10 < x < -5', ' '*45, '5 < x < 10')
        print('\t'*3 ,lproc1, ' '*50, lproc2)


flag()
usor(2)
func(10)
diag()