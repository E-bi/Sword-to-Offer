import queue
q = queue.Queue()
for i in range(10):
    q.put(i)
i = 0
while i<4:
    print(q.get())
    i += 1
print(q)
