#
# Brandi Rosser
# 05/28/2023
# Lab 03 Part 3
#
#

inputting = True
while inputting:
    workbooks = int(input("Enter number of workbooks: "))
    if workbooks in range(41):
        inputting = False
    else:
        print("Number of workbooks must be between 0 and 40.")

inputting = True
while inputting:
    textbooks = int(input("Enter number of textbooks: "))
    if textbooks in range(11):
        inputting = False
    else:
        print("Number of textbooks must be between 0 and 10.")

inputting = True
while inputting:
    magazines = int(input("Enter number of magazines: "))
    if magazines in range(26):
        inputting = False
    else:
        print("Number of magazines must be between 0 and 25.")

workbook_cost = 8.50
textbook_cost = 24.00
magazine_cost = 5.95

before_tax = 0
before_tax += workbook_cost * workbooks
before_tax += textbook_cost * textbooks
before_tax += magazine_cost * magazines

sales_tax = before_tax * 0.06

after_tax = before_tax + sales_tax

print(f"Cost before tax: ${before_tax:.2f}")
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Cost after tax: ${after_tax:.2f}")
