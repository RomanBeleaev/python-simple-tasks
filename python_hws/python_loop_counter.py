import os

os.system('cls')

start = int(input('start > '))
end = int(input('end > '))
step = int(input('step > '))
direction = start <= end
n = start

print(f'Counting from {start} to {end} with step {step}')

match direction:
    case True:
        while n <= end:
            print(n)
            n += step
    case False:
        while n >= end:
            print(n)
            n -= step
