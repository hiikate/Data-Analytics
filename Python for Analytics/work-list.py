## my work list
print('\nrandom list')
x = [4,8,10,3,5,0]
print(x)

# adding to the list
print('\nadded new numbers')
x.append(99)
x.append(11)
x.append(1)
print(x)

# sorting the list
print('\na sorted list')
x.sort()
print(x)

print('\ntuple')
y = 0
while y < len(x):
    print(x[y])
    y += 1
