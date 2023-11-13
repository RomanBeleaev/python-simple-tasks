import random

N = random.randint(1,10)

for tries in range(1,6):
    n = int(input( str(tries) + ') Guess ? >>> '))
    if n == N:
        print('Yes!\nYou win!')
        break
    elif n < N:
        print('Try greater')
    elif n > N:
        print('Try lesser')
    elif tries == 6 & n != N :
        print ('Game Over\nThe correct answer was:', N)