from math import gcd

N, S = map(int, input().split())
t = list(map(int, input().split()))

g = abs(t[0] - S)
for i in t[1:]:
    g = gcd(abs(i-S), g)
print(g)