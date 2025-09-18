print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
path = input("You stand in the sand and after a few steps you came across two paths: \nThe left path that leads to another part of the island across the beach and right path that leads to a forest. \nWhich you will choose? The Beach path or the Forest path?\n Type Beach or Forest? ")
if path == "Beach":
    print("After walking for 2 hours, the only thing you found is that you are completely lost!.\nGame over.\n")
else:
    house = input("You arrive at a cabin, out of nowhere in the middle of the forest. As soon as you get close to the house, you see 3 doors with different colors: one yellow, one red and one blue.\n Which one you will choose? Please type Red Yellow or Blue ")
    if house == "Red":
        print("As soon as you cross the door, it abruptly closes, without giving you a chance to stop it. You start hearing distant voices and they are coming closer each second, you start to run from these voices and suddenly you fall into a hole. \nGame over.\n")
    elif house == "Blue":
        print("You are pushed inside the house, you try to move but can't, you feel as you are under water and after a few second you lose consciousness. \nGame over.\n")
    elif house == "Yellow":
        print("As soon as you open the door, you are blasted with an intense yellow flash that almost blinds you. After a few seconds now you see a yellow chest. Congratulations, you found the treasure!")
