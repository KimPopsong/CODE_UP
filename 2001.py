pasta = []
juice = []

for i in range(3):
    pasta.append(int(input()))

for i in range(2):
    juice.append(int(input()))

pasta.sort()
juice.sort()

sum = pasta[0] + juice[0]

sum += sum / 10

print('%.1f'%sum)
