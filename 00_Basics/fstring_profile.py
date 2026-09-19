name = input("Name: ")
age = int(input("Age: "))
score = float(input("Score: "))
money = int(input("Money: "))
progress = float(input("Progress: "))
adult = age >= 20

print("=" * 50)
print(f"{'PYTHON PROFILE':^50}")
print("=" * 50)

print(f"{'Name':<15}{name:>15}")
print(f"{'Age':<15}{age:>15}")
print(f"{'Next Age':<15}{age + 1:>15}")
print(f"{'Score':<15}{score:>15.2f}")
print(f"{'Money':<15}{money:>15,}")
print(f"{'Progress':<15}{progress:>15.1%}")
print(f"{'Adult':<15}{str(adult):>15}")

print("=" * 50)



