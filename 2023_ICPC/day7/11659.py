# input보다 readline이 더 뻐름
import sys
input =  sys.stdin.readline

n, m = map(int, input().split())
nList = list(map(int, input().split()))
prefix_sum = [0]
# Prefix Sum
# 각각의 합들을 새로운 배열에다가 저장해뒀다가 나중에 입력이 들어오면 index로 바꿔서 출력
# 매 입력이 들어올 때마다, [j, i]의 구간 합은 p[i] - p[j-1] => O(1)
temp = 0
for i in nList:
    temp += i
    prefix_sum.append(temp)
# 예시의 경우, 최종 prefix_sum은 [0, 5, 9, 12, 14, 15] 이다.

for _ in range(m):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i-1])
