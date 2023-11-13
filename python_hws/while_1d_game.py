
map_lenght = 20
w = 8
x = 3
while True:
    print()
    n = 1
    if w == x:
        print('BOOOOM!!!')
        break
    else:
        while n <= map_lenght:
            if n == w:
                print ('W', end = ' ')
            elif n == x:
                print ('x', end = ' ')
            else:
                print ('~', end = ' ')
            n += 1

    print()

#   VVV Interaction VVV
    direction = input('inter direction (a/d) > ')
    match direction:
        case 'a':
            if w == 1:
                w = map_lenght
            else:
                w -= 1
        case 'd':
            if w == map_lenght:
                w = 1
            else:
                w += 1