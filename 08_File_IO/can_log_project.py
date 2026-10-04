

while True:
    print("=== CAN Log ===")
    print("1. Add Log")
    print("2. Show Log")
    print("3. Exit")

    menu = int(input("Menu: "))

    if menu == 1:
        can_id = input("CAN ID: ")
        can_data = input("DATA: ")

        with open("can_log.txt", "a") as file:
            file.write(f"{can_id}, {can_data}\n")

    elif menu == 2:
        with open("can_log.txt", "r") as file:
            for line in file:
                print(line.strip())

    elif menu == 3:
        print("Program Down")
        break

    else:
        print("Invalid Menu")


