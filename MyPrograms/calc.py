value1 = input("Enter Value: ")
value2 = input("Enter Value: ")
operator = input("Enter maths operator: ")

if operator == "+":
    sum = (float(value1) + float(value2))
    print("You have entered '+' operator")
    print(sum)
elif operator == "*":
    sum = (int(value1) * int(value2))
    print("You have entered '*' operator")
    print(sum)
elif operator == "/":
    sum = (int(value1) / int(value2))
    print("You have entered '/' operator")
    print(sum)
elif operator == "-":
    sum = (int(value1) - int(value2))
    print("You have entered '-' operator")
    print(sum)
else:
    print("Please enter the correct operator")


