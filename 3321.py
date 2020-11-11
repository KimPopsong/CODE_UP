import math

toppingKind = int(input())
s = input().split()

doughPrice = int(s[0])
toppingPrice = int(s[1])
doughKcal = int(input())
toppingKcal = []

for i in range(toppingKind):
    toppingKcal.append(int(input()))

toppingKcal.sort()

sumPrice = doughPrice
sumKcal = doughKcal
bestPizza = math.floor(sumKcal / sumPrice)  # When no topping

for i in range(toppingKind):
    sumPrice = doughPrice
    sumKcal = doughKcal

    for j in range(i, toppingKind):
        sumPrice += toppingPrice
        sumKcal += toppingKcal[j]

    if math.floor(sumKcal / sumPrice) > bestPizza:
        bestPizza = math.floor(sumKcal / sumPrice)

print(bestPizza)
