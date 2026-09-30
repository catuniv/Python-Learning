speed_data = [55, 72, 88, 91, 64]

while True:
    print("\n=== Sensor Data Menu ===")
    print("1. Show Data")
    print("2. Add Speed")
    print("3. Average Speed")
    print("4. Max / Min")
    print("5. OverSpeed Count")
    print("6. Exit")

    select = int(input("Menu: "))

    if select == 1:
        for value in speed_data:
            print(value, end=" ")

        print()

    elif select == 2:
        add = int(input("Add: "))
        speed_data.append(add)
        print()

    elif select == 3:
        avg = sum(speed_data) / len(speed_data)
        print(f"Average Speed is {avg}")
        print()

    elif select == 4:
        print(max(speed_data))
        print(min(speed_data))
        print()

    elif select == 5:
       count = 0

       for value in speed_data:
           if value >= 80:
               count += 1

       print(f"OverSpeed Count: {count}") 
       print()

    elif select == 6:
        print("Program end\n")
        break

    else:
        print("Invalid menu\n")
