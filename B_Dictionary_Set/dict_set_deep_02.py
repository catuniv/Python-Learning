can_logs = [
        ("0x100", "AA"),
        ("0x200", "BB"),
        ("0x100", "CC"),
        ("0x300", "DD"),
        ("0x200", "EE"),
        ("0x100", "FF")
]

groups = {}

for can_id, data in can_logs:
    groups.setdefault(can_id, []).append(data)


print("=== CAN LOG GROUP ===")
for can_id, data_list in groups.items():
    print(f"{can_id}: {data_list}")
