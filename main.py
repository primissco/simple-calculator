import os
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

firstnumber = float(input("Put in your first number:    "))
clear()
print(f"First number: {firstnumber}")
secondnumber = float(input("Put in your second number:    "))
clear()
print(f"First number: {firstnumber}")
print(f"Second number: {secondnumber}")
calc = str(input("What do you want to do with them? (+,-,*,/):  "))
clear()

if calc == "+":
    print(f"{firstnumber} + {secondnumber} = {firstnumber + secondnumber}")
elif calc == "-":
    print(f"{firstnumber} - {secondnumber} = {firstnumber - secondnumber}")
elif calc == "*":
    print(f"{firstnumber} * {secondnumber} = {firstnumber * secondnumber}")
elif calc == "/":
    print(f"{firstnumber} / {secondnumber} = {firstnumber / secondnumber}")

input()