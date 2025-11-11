# Write a program that checks if a number is positive/negative/zero
num = int(input("enter the number: "))
if num < 0:
    print("it is a NEGATIVE NUMBER")
elif num > 0:
    print("it is a POSTIVE NUMBER")
else:
    print("it is ZERO")


# if a user is eligible to vote
age = int(input("Enter your age :"))
if age >= 18:
    print("you are eligible to vote")
elif age < 18:
    print("you are not eligible to vote")
