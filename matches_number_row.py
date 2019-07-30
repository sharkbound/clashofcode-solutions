n = int(input())
c = 0
for i in range(n):
    row = input()
    c += sum(1 for x in map(int, row.split()) if x == i)
print(c)
