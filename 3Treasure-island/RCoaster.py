# print("Welcome to the roller coaster!")
# height = int(input("Enter your height\n"))
# age = int(input("Enter your age\n"))
# if height > 120:
#     print("Congratulations!! You can ride")
#     if age > 18:
#         print("Please pay $12")
#     else:
#         print("Please pay $7")
# else:
#     print("Sorry!! You can't ride")


print("Welcome to the roller coaster!")
height = int(input("Enter your height\n"))
if height > 120:
    print("Congratulations!! You can ride")
    age = int(input("Enter your age\n"))
    if age > 18:
        print("Please pay $12")
    elif age < 12:
        print("Please pay $5")
    else:
        print("Please pay $7")
else:
    print("Sorry!! You can't ride")

