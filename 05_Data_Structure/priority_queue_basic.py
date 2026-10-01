import heapq

queue = []

heapq.heappush(queue, (3, "Normal"))
heapq.heappush(queue, (1, "Attack"))
heapq.heappush(queue, (2, "Warning"))

for i in range(len(queue)):
    priority, message = heapq.heappop(queue)
    print(message)
    





