# print("Welcome to Treasure island.  ***  Your mission is to find the treasure.")

# direction = input("You want to go left or right?\n")
# if direction == "right":
#     print("GAME OVER!!")
# if direction == "left":
#     swim = input("Do you want to swim or wait?\n")
#     if swim == "swim":
#         print("GAME OVER!!")
#     else:
#         door = input("Choose a door. RED, BLUE or YELLOW?\n")
#         if door == "red":
#             print("GAME OVER!!")
#         elif door == "blue":
#             print("GAME OVER!!")
#         else:
#             print("YOU WIN..!!")

print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure island.  ***  Your mission is to find the treasure.")

direction = input('You\'re at a crossroad, Where do you want to go? Type "left" or "right"\n').lower()

if direction == "left":
    swim = input('You\'ve come to a lake. There is an island in the middle of the lake. Do you want to "swim" or "wait"?\n').lower()
    if swim == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors. Choose a door: RED, BLUE or YELLOW?\n").lower()
        if door == "red":
            print("Its a room full of fire. GAME OVER!!")
        elif door == "blue":
            print("You enter a room full of beasts. GAME OVER!!")
        elif door == "yellow":
            print("Congratulations you have found the treasure. YOU WIN..!!")
        else:
            print("You choose a door that doesn't exists. GAME OVER!!")
    else:
        print("You got attacked by an angry trout. GAME OVER!")
else:
    print("You fell into a hole. GAME OVER!")