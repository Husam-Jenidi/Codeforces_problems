group = 1
prev = ''
for _ in range(int(input())):
    curr = input()
    if curr != prev:
        group += 1
        prev = curr
print(group)
