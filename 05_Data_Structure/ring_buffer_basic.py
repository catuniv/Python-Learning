from collections import deque

buffer = deque(maxlen=5)

for i in range(7):
    data = int(input(f"Data {i + 1}: ")) 
    
    if buffer:
        avg = sum(buffer) / len(buffer)
        print(f"Average: {avg}")
        
        if abs(data - avg) >= 30:
             print("Status: ALERT")
        else:
             print("Status: NORMAL")

    buffer.append(data)
 
    print()


