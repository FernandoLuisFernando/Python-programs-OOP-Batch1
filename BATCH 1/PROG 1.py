# Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.
num1 = int(input("input yout first value: "))
num2 = int(input("input yout second value: "))
if num1 < num2: 
    print(f"{num2} is greater than {num1}")
else:
    print(f"{num1} is greater than {num2}")