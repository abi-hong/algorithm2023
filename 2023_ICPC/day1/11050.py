import sys
input =  sys.stdin.readline

n, k = map(int, input().split())

# 이항계수 구하기
def factorial(n):
  if (n == 0):
    return 1
  return n * factorial(n - 1)

print(factorial(n) // (factorial(k) * factorial(n - k)))