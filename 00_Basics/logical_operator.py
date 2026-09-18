
age = int(input("Age: "))
score = float(input("Score: "))

print("Adult and Passed: ", (age >= 20) and (score >= 80))
print("Adult or Passed: ", (age >= 20) or (score >= 80))
print("Not Adult: ", not(age >= 20))
print("Valid: ", (age >= 0) and (0 <= score <= 100))


