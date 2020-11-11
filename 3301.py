exchange = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

money = int(input())
count = 0
node = 0

while node < 8:
    if int(money / exchange[node]) > 0:
        money -= exchange[node]
        count += 1

    else:
        node += 1

print(count)
