import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("What do you choose? Type 0 for ROCK, 1 for PAPER or 2 for SCISSORS.\n"))

if choice >= 3 or choice < 0:
    print("INVALID CHOICE!!")
elif choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)
    

print("computer chose:")

moves = [rock, paper, scissors]
rand = random.choice(moves)

print(rand)

if choice == 0 and rand == rock:
    print("DRAW")
elif choice == 1 and rand == paper:
    print("DRAW")
elif choice == 2 and rand == scissors:
    print("DRAW")
elif choice == 0 and rand == scissors:
    print("YOU WIN")
elif choice == 0 and rand == paper:
    print("YOU LOSE")
elif choice == 1 and rand == rock:
    print("YOU WIN")
elif choice == 1 and rand == scissors:
    print("YOU LOSE")
elif choice == 2 and rand == rock:
    print("YOU LOSE")
elif choice == 2 and rand == paper:
    print("YOU WIN")