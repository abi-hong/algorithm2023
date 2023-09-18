# Ai의 오큰수는 
# 1. 오른쪽에 있으면서 2. Ai보다 큰 수 중에서 3. 가장 왼쪽에 있는 수
# 그러한 수가 없는 경우에 오큰수는 -1이다.
'''
- 이중 for문의 경우, 시간초과남
for i in range(n):
  for j in range(i+1, n):
    if (rbn[i] < rbn[j]):
      bigNum = rbn[j]
      result.append(bigNum)
      break
  else:
    result.append(-1)

- O(N*2)을 스택을 이용해서 O(N)으로 만드는게 관건
stack에는 원소값이 아닌 원소의 인덱스를 넣어주는 목적으로 사용
'''

n = int(input())
rbn = list(map(int, input().split()))
stack = []
result = [-1] * n

stack.append(0)
for i in range(n):
  print('i', i, 'stack', stack)
  while stack and (rbn[stack[-1]] < rbn[i]):
    print('i', i, 'stack[-1]', stack[-1], 'rbn[i]', rbn[i])
    result[stack[-1]] = rbn[i]
    stack.pop()
  stack.append(i)


for a in result:
  print(a, end=" ")