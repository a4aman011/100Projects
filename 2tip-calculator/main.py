# score = 0
# height = 1.8
# isWinning = True
# print(f"your score is {score} your height is {height} and your winning is {isWinning}")


print("Welcome to the tip calculator")
bill = float(input("Enter the bill amount\n"))
tip = int(input("Enter the tip percentage. 10, 12 or 15\n"))
people = int(input("How many people the bill be divided into?\n"))

newTip = tip/100 * bill
newBill = bill + newTip
billPerPerson = newBill/people
# print(round(billPerPerson,2))
print(f"Your total bill per person is {billPerPerson}")