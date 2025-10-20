for i in range(6):
    if i not in range(2,4):
        print('\x1b[48;5;231m        ',end=' ')
        print('\x1b[48;5;21m    ',end='')
        print('\x1b[48;5;231m        ',end=' ')
        print('\x1b[0;5;0m')
    else:
        print('\x1b[48;5;21m                      ',end='')
        print('\x1b[0;5;0m')


