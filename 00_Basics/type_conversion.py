
print("=== TYPE CONVERSION ===")

number = int(input("Integer: "))
print(f"Integer Type: {type(number)}")

real = float(input("Float: "))
print(f"Float Type: {type(real)}")

text = input("Text: ")
print(f"Text Type: {type(text)}")

print(f"Integer Bool: {bool(number)}")
print(f"Text Bool: {bool(text)}")

print(f"Zero Bool: {bool(0)}")
print(f"Empty String Bool: {bool("")}")


