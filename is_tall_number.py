n = input()
l = int(n[0])
for d in map(int, n[1:]):
    if d < l:
        print('false')
        break
    l = d
else:
    print('true')
