s = input().split()

now = int(s[0])
goal = int(s[1])

count = 0

if now > goal:
    now, goal = goal, now

while True:
    if goal - now > 7:
        now += 10
        count += 1

    else:
        if goal < now:
            goal, now = now, goal
        break

while True:
    if goal - now >= 3:
        now += 5
        count += 1

    else:
        if goal < now:
            goal, now = now, goal
        break

while now < goal:
    now += 1
    count += 1

print(count)
