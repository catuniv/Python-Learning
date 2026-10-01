stack = []

for i in range(3):
    num = int(input(f"Number {i+1}: "))
    stack.append(num)


print(f"Stack: {stack}\n")

value = stack.pop()

print(f"Removed: {value}")
print(f"Stack: {stack}")


    
