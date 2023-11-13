food_1_name = "pizza"
food_1_price = 75.00

food_2_name = "salad"
food_2_price = 15.50

delivery_price = 100

#print Menu
print("########## Menu ##########")
print(f'1 {food_1_name} : {food_1_price}')
print(f'2 {food_2_name} : {food_2_price}')
print("##########################")

option = input("Choose >>> ")

if option == "1":
    print(f'You have chosen {food_1_name}')
    quantity = int(input("How many do you want? >>> "))
    cost = quantity * food_1_price
    print(f'Cost: {cost}')

    delivery = input("Do you want delivery? y/n >>> ")

    if delivery == "y":
        if cost >= 500:
            print("Delivery is FREE")
        else: 
            cost += delivery_price
            print(f'Cost with delivery: {cost}')

elif option == "2":
    print(f'You have chosen {food_2_name}')
    quantity = int(input("How many do you want? >>> "))
    cost = quantity * food_2_price
    print(f'Cost: {cost}')

    delivery = input("Do you want delivery? y/n >>> ")

    if delivery == "y":
        if cost >= 500:
            print("Delivery is FREE")
        else: 
            cost += delivery_price
            print(f'Cost with delivery: {cost}')