# Python money converter

money = float(input("Enter your money:   "))
unit = input("Dollars or Pesos? (D or P):   ")

if unit == "D":
    money = money * 20
    unit = "Pesos"
elif unit == "P":
    money = money / 20
    unit = "Dollars"
else:
    print(f"{unit} was not valid")

print(f"Your money is: {round(money, 1)} {unit}") 
