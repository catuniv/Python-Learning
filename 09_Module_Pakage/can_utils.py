
allowed_ids = {"0x100", "0x200", "0x300"}


def perse_can(data):
    can_id, payload = data.split(",")

    can_id = can_id.strip()
    payload = payload.strip()

    return can_id, payload
   
def is_allowed(can_id):
    return can_id in allowed_ids

