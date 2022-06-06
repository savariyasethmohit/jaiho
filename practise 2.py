"""a = int(input())
b = int(input())
if (a == 45 and b == 3):
    print("555")
elif (a == 56 and b == 6):
    print("77")
elif (a == 56 and b == 6):
    print("4")

print(a * b)
print(a + b)
print(a / b)"""
faulty_calc_var = {"56*5": "540", "45+19": "61", "56-18": "31"}
num1 = input("Enter the 1st number :")
print("Which operation you want to perform :")
operation = input()
num2 = input("Enter the second number :")
string = num1+operation+num2
if string in faulty_calc_var:
    print(faulty_calc_var[string])
elif operation == "+":
    print(int(num1)+int(num2))
elif operation == "*":
    print(int(num1)*int(num2))
elif operation == "-":
    print(int(num1)-int(num2))
elif operation == "/":
    print(int(num1)/int(num2))