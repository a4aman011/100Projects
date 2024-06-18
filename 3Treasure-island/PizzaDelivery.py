# print("Thank you for choosing Python Pizza Deliveries!\n")
# size = input("What size pizza do you want? S, M, or L\t")
# # s = 15
# # m = 20
# # l = 25
# if size == "s":
#     bill = 15
#     peproni = input("Do you want pepperoni? Y or N\t")
#     if peproni == "y":
#         bill += 2
#     cheese = input("Do you want extra cheese? Y or N\t")
#     if cheese == "y":
#         bill += 1
# elif size == "m":
#     bill = 20
#     peproni = input("Do you want pepperoni? Y or N\t")
#     if peproni == "y":
#         bill += 3
#     cheese = input("Do you want extra cheese? Y or N\t")
#     if cheese == "y":
#         bill += 1
# else:
#     bill = 25
#     peproni = input("Do you want pepperoni? Y or N\t")
#     if peproni == "y":
#         bill += 3
#     cheese = input("Do you want extra cheese? Y or N\t")
#     if cheese == "y":
#         bill += 1

# print(f"Your final bill is ${bill}")


print("Thank you for choosing Python Pizza Deliveries!\n")
size = input("What size pizza do you want? S, M, or L:-\t")
bill = 0
if size == "s":
    bill = 15
elif size == "m":
    bill = 20
else:
    bill = 25

peproni = input("Do you want pepperoni? Y or N\n")
if peproni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

cheese = input("Do you want extra cheese? Y or N\n")
if cheese == "y":
    bill +=1

print(f"Your final bill is ${bill}")