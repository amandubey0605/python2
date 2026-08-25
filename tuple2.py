# WAP to count the number of zeros in the given tuple. a=(7,0,8,0,0,9)
a=(7,0,8,0,0,9)
print(f'numbers of zeros:{a.count(0)}')


# OR
a = (7, 0, 8, 0, 0, 9)

count = 0
for i in a:
    if i == 0:
        count += 1

print(f'number of zeros :{count}')