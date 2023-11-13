year_of_birth = int(input("Year of birth >> "))
if year_of_birth < 1900 or year_of_birth > 2023:
    print("Does not match the required range!!!")
else:
    age = 2023 - year_of_birth
    print(age)
    if age >= 0 and age <= 3:
        print("Baby")
    elif age >= 4 and age <= 9:
        print("Kid")
    elif age >= 10 and age <= 15:
        print("Teen")
    elif age >= 16 and age <= 18:
        print("Young")
    elif age >= 19 and age <= 50:
        print("Adult")
    else:
        print("Old")