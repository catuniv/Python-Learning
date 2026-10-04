from can_utils import perse_can, is_allowed

data = input("Data: ")
can_id, payload = perse_can(data)
allowed = is_allowed(can_id)

print(f"CAN ID: {can_id}")
print(f"Payload: {payload}")
print(f"Allowed: {allowed}")
