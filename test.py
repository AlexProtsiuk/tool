a = [0, 5, 'g', 'k', 89, '35']
b = [5, 'g', '35']
c = []

for i in range(0, len(a)):
    if a[i] in b:
        print('bingo!')
    else:
        c.append(a[i])

print(c)

cell = ' 18789 Батарейка alkaline Sony ALKALINE LR06(1*4) шт '
new_cell = cell.strip(' ')
print(cell)
print(new_cell)

a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
marker = ''
for i in range(len(new_cell)):
    if new_cell[i] in a:
        marker += new_cell[i]
    else:
        break

print(marker)
