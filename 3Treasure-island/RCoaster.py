# print("Welcome to the roller coaster!")
# height = int(input("Enter your height\n"))
# if height > 120:
#     print("Congratulations!! You can ride")
#     age = int(input("Enter your age\n"))
#     if age > 18:
#         print("Please pay $12")
#     elif age < 12:
#         print("Please pay $5")
#     else:
#         print("Please pay $7")
# else:
#     print("Sorry!! You can't ride")



print("Welcome to the roller coaster!")
height = int(input("Enter your height\n"))
bill = 0
if height > 120:
    print("Congratulations!! You can ride")
    age = int(input("Enter your age\n"))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age >= 45 and age <= 55:
        print("Everything will be okay. your bill is on us!")
    elif age > 18:
        bill = 12
        print("Adult tickets are $12")
    else:
        bill = 7
        print("Youth tickets are $7")

    photo = input("Do you want photos? Y or N. ")
    if photo == "y":
        bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("Sorry!! You can't ride")

