allowed_ids = {"0x100", "0x200", "0x300"}
count = {}

for i in range (5):
    new_id = input(f"CAN ID {i + 1}: ")
    
    if new_id in allowed_ids:
        print("ALLOWED")
    else:
        print("UNKWOWN")

    count[new_id] = count.get(new_id, 0) + 1



print("=== COUNT ===")

for key, value in count.items():
    print(f"{key}: {value}")
