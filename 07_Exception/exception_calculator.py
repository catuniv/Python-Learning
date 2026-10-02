

try:
    a = int(input("A: "))
    b = int(input("B: "))
    result = float(a / b)

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Cannot Divide by ZERO")

else:
    print(f"Result: {result}")


