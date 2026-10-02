
vehicle = input("Vehicle name: ")
distance = float(input("Distance(km): "))
time = float(input("Time(hour): "))
fuel = float(input("Fuel(L): "))

avgS = distance / time
fe = distance / fuel

if avgS >= 80:
    status = "FAST"
elif avgS >= 40:
    status = "NORMAL"
else:
    status = "SLOW"

while True:
        print("\n=== Vehicle Information ===")
        print("1. Average Speed")
        print("2. Fuel Efficiency")
        print("3. Driving Status")
        print("4. Show All")
        print("5. Exit")
        
        print()
        select = int(input("Menu: "))

        if select == 1:
            print(f"\nAverage Speed: {avgS:.2f}Km/h")
            
        elif select == 2:
            print(f"\nFuel Efficiency: {fe:.2f}Km/L")

        elif select == 3:
            print(f"Driving Status: {status}")

        elif select == 4:
            print(f"\n=== {vehicle} Information ===")
            print(f"Distance: {distance:.2f} km")
            print(f"Time: {time:.2f} hour")
            print(f"Fuel: {fuel:.2f} L")
            print(f"Average Speed: {avgS:.2f} km/h")
            print(f"Fuel Efficiency: {fe:.2f} km/L")
            print(f"Driving Status: {status}")
        
        elif select == 5:
            print("Program end")
            print()
            break;
      
        else:
            print("Invalid Menu")
