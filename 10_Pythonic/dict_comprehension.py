can_data = {
        "0x100": 60,
        "0x200": 120,
        "0x300": 90,
        "0x400": 150
}

# only 100 high

result = {
        can_id: can_speed
        for can_id, can_speed in can_data.items()
        if can_speed >= 100
}

print(result, end='\n')

