from collections import deque

# A를 B로 바꾸는데 필요한 연산의 최솟값
a, b = map(int, input().split())
result = 0
q = deque()
q.append((a,1))

# top-down으로 생각해야함 -> b를 a로
while (b != a):
  result += 1
  temp = b
  if (b % 10 == 1):
    b //= 10
  elif (b % 2 == 0):
    b //= 2
  
  if temp == b:
    print(-1)
    break
else:
  print(result + 1)

# bfs -> bottom-up
# pop한 원소가 b와 같다면, 멈춘 뒤 연산 횟수 출력
'''
while q:
  n, t = q.popleft()
  if n > b:
    continue
  if n == b:
    print(t)
    break
  q.append((int(str(n) + "1"), t + 1))
  q.append((n * 2, t + 1))
  x = q.popleft()
else:
  print(-1)
'''