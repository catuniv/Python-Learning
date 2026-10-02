speed_data = [55, 72, 88, 91, 64]


def show_data(data):
    for value in data:
        print(value)


def add_speed(data):
    add = int(input("Add: "))
    data.append(add)
    print("Add Success")

def average_speed(data):
    avg = sum(data) / len(data)
    return avg
    

def max_min(data):
    max_value = max(data)
    min_value = min(data)

    return max_value, min_value


while True:
    print("\n===== Funtion ====")
    print("1. Show Data")
    print("2. Add Speed")
    print("3. Average Speed")
    print("4. Max / Min")
    print("5. Exit")

    menu = int(input("Menu: "))

    if menu == 5:
        print("Program end")
        break

    elif menu == 1:
        show_data(speed_data)

    elif menu == 2:
        add_speed(speed_data)

    elif menu == 3:
        avg = average_speed(speed_data)
        print(f"Average: {avg:.2f}")

    elif menu == 4:
        max_value, min_value = max_min(speed_data)
        print(f"Max: {max_value}")
        print(f"Min: {min_value}")

    else:
        print("Invalid Menu")

