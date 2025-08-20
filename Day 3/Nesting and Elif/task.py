print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age?"))

if height >= 120:
    if age >= 18:
        print("You can ride and your ticket cost is $12")
    elif age >=12:
        print("Your ticket cost is $10")
    else:
        print("You can ride and your ticket cost is $7")
else:
    print("Sorry you have to grow taller before you can ride.")
