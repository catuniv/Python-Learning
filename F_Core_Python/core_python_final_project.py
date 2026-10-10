from collections import deque

allowed_ids = {"0x100", "0x200", "0x300"}
speed_buffer = deque(maxlen=5)

can_logs = []

def add_can_log(data):
    can_id, speed, rpm = data.split(",")
    speed = int(speed)
    rpm = int(rpm)

    log = {
            "id": can_id,
            "speed": speed,
            "rpm": rpm
    }

    can_logs.append(log)
    speed_buffer.append(speed)
    return


while True:
    print("=== CAN MONITOR ===")
    print("1. Add CAN Log")
    print("2. Show Logs")
    print("3. Show ID Count")
    print("4. Show Recent Speed")
    print("5. Check Unkown IDs")
    print("6. EXIT")
    menu = int(input("Menu: "))

    if menu == 6:
        print("Program Down")
        break

    elif menu == 1:
        data = input("CAN Data: ")
        add_can_log(data)

    elif menu == 2:
        for log in can_logs:
            print(f"ID: {log['id']}, Speed: {log['speed']}, RPM: {log['rpm']}")


    elif menu == 3:
        count = {}

        for log in can_logs:
            can_id = log["id"]
            count[can_id] = count.get(can_id, 0) + 1

        for can_id, value in count.items():
            print(f"{can_id}: {value}")


    elif menu == 4:
        if speed_buffer:
            print(f"Recent: {speed_buffer}")
            avg = sum(speed_buffer) / len(speed_buffer)
            print(f"Average: {avg:.2f}")
        else:
            print("No Speed Data")




    elif menu == 5:
        received_ids = set()
       
        for log in can_logs:
            received_ids.add(log["id"])

        U_id = received_ids - allowed_ids
        print(f"Unknown IDs: {U_id}")

    else:
        print("Invalid Menu")


