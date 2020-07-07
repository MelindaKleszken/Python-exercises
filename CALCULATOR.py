print("Select operation.")
print("A.Add")
print("S.Subtract")
print("M.Multiply")
print("D.Divide")


choice = input("Enter choice(A/S/M/D): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

add = num1 + num2
substract = num1 - num2
multiply = num1 * num2
divide = num1 / num2

if choice == 'A':
   print(num1,"+",num2,"=", add)

elif choice == 'S':
   print(num1,"-",num2,"=", substract)

elif choice == 'M':
   print(num1,"*",num2,"=", multiply)

elif choice == 'D':
   print(num1,"/",num2,"=", divide)
else:
   print("Invalid input")