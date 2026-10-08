def analyze_speed(*args):
    total = sum(args)
    avg = total / len(args)
    max_speed = max(args)

    return total, avg, max_speed

total, avg, max_speed = analyze_speed(80, 90, 120, 70)

print(f"Total: {total}")
print(f"Average: {avg:.2f}")
print(f"Max: {max_speed}")

