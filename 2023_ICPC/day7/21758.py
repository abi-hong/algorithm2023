from copy import deepcopy

n = int(input())
honey = list(map(int, input().split()))
s = deepcopy(honey)
maxSum = 0

# 누적합을 미리 구하고 시작하기
for i in range(1, n):
    s[i] += s[i-1]

# 장소들 중 서로 다른 두 곳을 골라서 벌을 한 마리씩 둔다
# 다른 한 장소를 골라서 벌통을 둔다.
### 경우의 수(3가지)
# 1. 벌벌꿀
#    한 마리는 첫번째 위치 고정, 벌통은 마지막 위치 고정
#    왜냐하면 벌은 자신 이전 위치의 꿀은 따지 못하기에
#    벌통과 최대한 멀리 떨어져있는 곳에서 시작하는 것이 이득
#    나머지 벌의 경우, 반복문으로 해당 위치를 바꿔가면 최댓값이 나오면 갱신해야 한다.
for i in range(1, n-1):
    maxSum = max(maxSum, 2*s[-1] - honey[i] - honey[0] - s[i])

# 2. 꿀벌벌
#    한 마리는 마지막 위치 고정, 벌통은 첫번째 위치 고정
for i in range(1, n-1):
    maxSum = max(maxSum, s[-1] - honey[-1] - honey[i] + s[i-1])

# 3. 벌꿀벌
#    한 마리는 첫번째 위치 고정, 두번째는 마지막 위치 고정
for i in range(1, n-1):
    maxSum = max(maxSum, s[i] - honey[0] + s[-1] - s[i-1] - honey[-1])

print(maxSum)