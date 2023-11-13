start_n = input("Start position of counting >>")
end_n = input("End position of counting >>")
n = start_n
if start_n < end_n:
    while n <= end_n:
        print(n)
        n += 1
else:
    while n >= end_n:
        print(n)
        n -= 1