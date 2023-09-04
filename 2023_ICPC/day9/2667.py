n = int(input())
graph = []
num = []
count = 0 # 단지 내 집의 수
result = 0 # 단지 개수

for i in range(n):
    graph.append(list(map(int, input())))
# or graph = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    if (x < 0 or x >= n or y < 0 or y >= n):
        return False
    if graph[x][y] == 1: # 집이 있다.
        global count
        count += 1
        graph[x][y] = 0 # 다시 방문하지 않도록
        for i in range(4):
            # (x-1, y), (x+1, y), (x, y+1) ,(x, y-1)
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            #print('i', i, 'j', j)
            num.append(count)
            result += 1
            count = 0

num.sort()
print(result)
for i in range(len(num)):
    print(num[i])