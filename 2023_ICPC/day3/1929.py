import sys

input = sys.stdin.readline
m, n = map(int,input().split())

for i in range(m, n+1):
  if i == 1:
    continue
  for j in range(2, int(i**0.5)+1):
    # 범위는 2부터 int(i**0.5)+1까지이다. 
    # 특정 수의 제곱근을 구해, 그 제곱근까지의 약수를 구하면 해당 약수를 포함하는 수를 모두 제거할 수 있다(소수가 아니기에).
    if i % j == 0:
      break
  else:
    print(i)