
can_ids = ["0x100", "0x200", "0x300"]
status = ["NORMAL", "ATTACK", "WARNING"]

for can_id, status in zip(can_ids, status):
    print(f"{can_id} -> {status}")
