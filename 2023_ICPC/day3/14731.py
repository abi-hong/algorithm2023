n = 10**9 + 7

m = int(input())

#시간 초과 떠서 분할정복 사용해서 거듭제곱 계산해줘야함
sum = 0

def calculate_pow(a, b, c):
     if (b < 0):
          return 0
     result = 1
     cur = a
     while b:
          if (b & 1):
               result = result * cur % c
          cur = cur * cur % c
          b //= 2
     return result
          

for _ in range(m):
    c, k = map(int, input().split())
    sum += c * k * calculate_pow(2, k-1, n)

print(sum%n)