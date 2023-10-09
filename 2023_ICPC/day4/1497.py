from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
guitars = set()

for _ in range(n):
  name, song = input().split()
  change_int = ''
  for i in song:
    if i == 'Y':
      change_int += '1'
    else:
      change_int += '0'
  guitars.add(int(change_int, 2))

guitars -= {0} # set에서 0 제거

if not guitars:
  print(-1)
  exit(0)

max_count = 0
for i in range(1, n+1):
  for comb in combinations(guitars,i):
    # total에 각각 조합마다 이진수 연산
    total = 0
    for num in comb:
      total |= num

    # 연산한 total에서 Y몇개인지 확인.
    count = 0
    for j in range(m): # j = 0, 1, 2, 3, 4, 5
      # 부분집합의 경우의 수를 표현하는 이진수를 1<<j (j는 모든 인덱스 값)와 &연산 -> 1이면, 해당 부분집합에 포함된다는 뜻
      if total & (1<<j):
        count += 1
      if max_count < count:
        max_count = count
        max_guitar = i

print(max_guitar)