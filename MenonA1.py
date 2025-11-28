# CS 7, Assignment 1, Section D01, 9/4/2024, Aditi Menon
# Part One: Hours Worked & Hourly Wage
hoursWorked = float(input("How many hours did you work last week? "))
hourlyWage = float(input("How much do you earn per hour? "))
pay = hoursWorked * hourlyWage
print(f"You earned ${pay:.2f}")
# Part Two: Centigrade to Fahrenheit
centigrade = float(input("What is the temperature in Centigrade? "))
fahrenheit = centigrade * (9/5) + 32
print(f"That's {fahrenheit}°F")
# Part Three: Cafeteria Items & Cost
id = input("Enter your ID number: ")
firstItem = input("Enter the first item you are buying: ")
costOne = float(input(f"Enter the cost of the {firstItem}: "))
secondItem = input("Enter the second item you are buying: ")
costTwo = float(input(f"Enter the cost of the {secondItem}: "))
thirdItem = input("Enter the third item you are buying: ")
costThree = float(input(f"Enter the cost of the {thirdItem}: "))
print(f"----------------Receipt for {id}------------------")
print(f"{firstItem} {costOne: .2f}")
print(f"{secondItem} {costTwo: .2f}")
print(f"{thirdItem} {costThree: .2f}")
sum = costOne + costTwo + costThree
print(f"subtotal {sum: .2f}")
tax = (sum * 10.25) / 100
print(f"tax {tax: .2f}")
print(f"total {(sum + tax): .2f}")
print("---------------------------------------------------")
