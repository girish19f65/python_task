num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
op = input("enter operator (+,-,*,/,**):")

if op == '+' and (num1 >= 0 or num1 <= 0) and (num2 >= 0 or num2 <= 0):
    print("sum =", num1+num2)
elif op == '-':
    print("subtraction =", num1-num2)
elif op == '*':
    print("multiplication =", num1*num2)
elif op == '/' and num2 != 0:
    print("Division =", num1/num2)
elif op == '**':
    print("Exponentiation", num1**num2)
else:
    print("invalid input or cannot divide by zero")
