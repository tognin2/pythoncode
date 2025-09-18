print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:  #or 45 <= age <= 55
        print("Ride is free")
    else:
        bill = 12
        print("Adult tickets are $12.")
    wants_photos = str(input("Do you want photos? Please type yes or no "))
    if wants_photos == "yes": ##then add $3 to the bill, but to do that I need to create a variable named "bill" first on the code
        bill += 3
        print(f"Your final bill is ${bill}")
    else:
        print("I hope you had a wonderful ride!")
else:
    print("Sorry you have to grow taller before you can ride.")
