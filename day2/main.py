# Welcome to the tip calculator

# Input total bill

# Input how much tip (10, 12, 15)

# Input how many people to split the bill

# Each person shouldp pay: x

print("Welcome to the tip calculator!")

total = float(input("What was the total bill? $"))

tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
tip_percentage = tip / 100

people = int(input("How many people to split the bill?"))

each = (total + total * tip_percentage) / people
each_rounded = round(each, 2)

print("Each person should pay: $" + str(each))