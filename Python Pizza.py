print("Welcome to Python Pizza Deliveries!")
bill = 0
size = input("What size pizza do you want? S, M or L: ")
if size == "S":
    bill = 15
    small_p = input("Add pepperoni for small pizza? (Y or N) ")
    if small_p == "Y":
        bill += 2

if size == "M":
    bill = 20

if size == "L":
    bill = 25

if bill >= 20:
    ml_p = input("Add pepperoni for medium or large pizza? (Y or N) ")
    if ml_p == "Y":
        bill += 3

extra_cheese = input("Do you want extra cheese? (Y or N) ")
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")

