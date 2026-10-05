
can_ids = ["0x100", "0x200", "0x999", "0x300"]

valid_ids = [new_ids for new_ids in can_ids if new_ids != "0x999"]

print(valid_ids)
