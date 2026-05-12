def hanoi(n, start, mid, target):
    if n == 1:
        print(f'{start} to {target}')
    else:
        hanoi(n-1, start, target, mid)
        print(f'{start} to {target}')
        hanoi(n-1, mid, start, target)

print('3 disks:')
hanoi(3, 0, 1, 2)

print('\n4 disks:')
hanoi(4, 0, 1, 2)