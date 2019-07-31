M = lambda: map(int, input().split())
n, x = M()
h = [0] * x
for i in range(n):
    a, b = M()
    for ind in range(a, b + 1):
        h[ind] += 1
print(min(h), max(h), sep='\n')
