sensor_status = {
        "camera": "ON",
        "lidar": "ON",
        "radar": "OFF"
}

while True:
    print("\n=== Sensor Menu ===")
    print("1. Show All")
    print("2. Change Status")
    print("3. Add Sensor")
    print("4. Delete Sensor")
    print("5. Show Active Sensors")
    print("6. Exit")

    menu = int(input("Menu: "))

    if menu == 1:
               for key, value in sensor_status.items():
                            print(key, value)

    elif menu == 2:
               temp = input("Sensor: ")
               power = input("ON/OFF: ")

               if temp in sensor_status:
                    print("Search Success")
                    sensor_status[temp] = power
                    print(f"Power {power}")
               else:
                    print("Search Failed")


    elif menu == 3:
               temp = input("Add Sensor Name: ")
               power = input("ON/OFF: ")
               sensor_status[temp] = power
   
    elif menu == 4:
               temp = input("Delete Sensor Name: ")

               if temp in sensor_status:
                        del sensor_status[temp]
               else:
                        print("Search Failed")

    elif menu == 5:
               active = set()

               for sensor, status in sensor_status.items():
                            if status == "ON":
                                    active.add(sensor)

               print(active)
                

    elif menu == 6:
               print("Program end")
               break

    else:
               print("Invalid Menu")

