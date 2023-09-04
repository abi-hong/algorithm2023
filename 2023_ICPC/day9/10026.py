from collections import deque

n = int(input())

graph = []
q = deque()
for i in range(n):
    graph.append(list(map(str, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수
def bfs(x, y):
  q.append((x, y))
  visited[x][y] = 1

  while q:
     x, y = q.popleft()
     for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 범위 안에 있고 같은 색이고 아직 방문하지 않은 경우 
        if (0 <= nx < n) and (0 <= ny < n) and (graph[nx][ny] == graph[x][y]) and (not visited[nx][ny]) :
           visited[nx][ny] = 1
           q.append((nx, ny))


# 적록색약이 아닌 경우
visited = [[0] * n for _ in range(n)]
cntNo = 0
for i in range(n):
   for j in range(n):
      if not visited[i][j]:
         bfs(i, j)
         cntNo += 1

# 적록색약인 경우
visited = [[0] * n for _ in range(n)]
cntYes = 0
for i in range(n):
   for j in range(n):
      if graph[i][j] == 'G':
         graph[i][j] = 'R'

for i in range(n):
   for j in range(n):
      if not visited[i][j]:
         bfs(i, j)
         cntYes += 1

print(cntNo, cntYes)