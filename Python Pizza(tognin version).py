print("Welcome to Python Pizza Deliveries!")
bill = 0
size = str(input("What size pizza do you want? S, M or L: "))
if size == "S":
    bill = 15
    print("A small pizza will cost $15")
wants_pepperoni_s = input("Add pepperoni for small pizza? (Y or N) ")
if wants_pepperoni_s == "Y":
    bill += 2
    print(f"Your currently bill is ${bill}")

if size == "M":
    bill = 20
    print("A medium pizza will cost $20")
wants_pepperoni_m = input("Do you want pepperoni on your medium pizza? Y or N: ")
if wants_pepperoni_m == "Y":
    bill += 3
    print(f"Your bill now is ${bill}")

if size == "L":
    bill = 25
    print("A large pizza will cost $25")
wants_pepperoni_l = input("Do you want pepperoni on large pizza? Y or N: ")
if wants_pepperoni_l == "Y":
    bill += 3
    print(f"Your bill now is ${bill}")

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    bill += 3
    print(f"Your final bill is ${bill}")

