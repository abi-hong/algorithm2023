from collections import deque

m, n = map(int, input().split())

# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸

graph = []
q = deque([])
day = 0

for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

'''
리스트를 돌면서 1을 발견하면 우선 큐에 저장해 두고 다 돌고 나서 BFS를 돌며 상하좌우 탐색을 한다. 
상하좌우에 안 익은 토마토(0)가 있다면 현재 arr[x][y]에서 1씩 추가하며 일수를 저장한다. 
마지막에 리스트에서 제일 큰 값에서 1을 뺀 값이 최소 날짜이다. (리스트를 돌 때 0이 아니라 1에서부터 추가해 올라갔기 때문에)
'''
# 1. 1인 좌표 큐에 저장하기
for i in range(n):
   for j in range(m):
      if (graph[i][j] == 1):
         q.append([i, j])

# 2. bfs를 통해 상하좌우 탐색
while q:
  x, y = q.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    
    if (0 <= nx < n) and (0 <= ny < m) and (graph[nx][ny] == 0):
       graph[nx][ny] = graph[x][y] + 1
       q.append([nx, ny])

for i in graph:
    for j in i:
      if (j == 0):
        print(-1)
        exit(0)
    day = max(day, max(i))
print(day - 1)