from collections import deque

queue = deque()

while True:
    print("=== CAN Queue ===")
    print("1. Add Message")
    print("2. Show Queue")
    print("3. Process Message")
    print("4. Exit")

    menu = int(input("Menu: "))

    if menu == 1:
        message = input("Message: ")
        queue.append(message)

    elif menu == 2:
        if queue:
            print(f"Queue: {queue}")     
        else:
            print("Queue is Empty")

    elif menu == 3:
        if queue:
            Fmessage = queue.popleft()
            print(f"Processed: {Fmessage}")
        else:
            print("Queue is Empty")

    elif menu == 4:
        print("Program End")
        break
    
    else:
        print("Invalid Menu")


