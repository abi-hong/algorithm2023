import sys
sys.setrecursionlimit(10**6)
input =  sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n + 1)
parent = [0] * (n + 1) # 부모 노드 저장할 배열

for _ in range(n-1):
  start, end = map(int, input().split())

  # 2차원 연결 리스트 - 양방향 연결 정보 저장
  graph[start].append(end)
  graph[end].append(start)

# 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력
def dfs(root):
  visited[root] = 1
  for neighbor in graph[root]:
    if not visited[neighbor]:
      parent[neighbor] = root
      dfs(neighbor)
dfs(1)

for i in range(2, n+1):
  print(parent[i])
