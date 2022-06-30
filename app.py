
weight = int(input("Weight: "))
unit = input("Please enter (K)g or (L)bs: ")

if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
elif unit.upper() == "L":
    converted = weight * 0.45
    print("Weight in Kg: " + str(converted))
else:
    print("Please enter the correct value")

print("*" * 5 + " Program End " + "*" * 5)

