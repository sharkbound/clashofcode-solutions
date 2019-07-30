t = int(input())
for i in range(t):
    s1, s2 = [int(j) for j in input().split()]
    print("Yes" if not s2 % s1 else "No")
