from collections import deque

queue = deque()

for i in range(3):
    number = int(input(f"Number{i+1}: "))
    queue.append(number)


print("Queue:", queue)

removed = queue.popleft()

print()
print(f"Removed: {removed}")
print("Queue:", queue)
