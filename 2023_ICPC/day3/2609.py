#python의 경우, math 모듈에 gcd가 내장되어 있다.
a, b = list(map(int, input().split()))

def gcd(x, y):
    while y:
        x, y = y, x%y
    return x

def lcm(x, y):
    return x * y // gcd(x,y)


print(gcd(a,b))
print(lcm(a, b))