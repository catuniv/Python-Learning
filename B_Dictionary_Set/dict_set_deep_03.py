allowed_ids = {"0x100", "0x200", "0x300", "0x400"}

received_ids = {
        "0x100",
        "0x200",
        "0x999",
        "0x777",
        "0x300"
}

print("=== CAN ID CHECK ===")
print("Allowed & Received:", allowed_ids & received_ids)
print("Unknown IDs:", received_ids - allowed_ids)
print("All Received IDs Allowed:", received_ids <= allowed_ids)


