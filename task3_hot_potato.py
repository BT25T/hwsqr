from collections import deque

s = input()
s = s.split(" with ")
queue, passes= deque(s[0].split(", ")), int(s[1][0])

while len(queue)>1:
    for i in range(passes):
        queue.append(queue.popleft())
    queue.popleft()
print(f"Winner: {queue[0]}")