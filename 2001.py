pasta = []
juice = []

for i in range(3):
    pasta.append(int(input()))

for i in range(2):
    juice.append(int(input()))

pasta.sort()  # sort by Ascending
juice.sort()  # sort by Ascending

sum = pasta[0] + juice[0]  # lowest price of pasta and juice

sum += sum / 10  # 10percent of sum

print('%.1f'%sum)  # .1f to show 
