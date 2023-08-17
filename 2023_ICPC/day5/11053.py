N = int(input())
A = list(map(int, input().split()))

dp = [0 for i in range(1000)]
ret = 0
# 초기조건 : dp[1] = 1
# dp[i] = max(dp[j] + 1)
# dp[i] := i번쩨 원소를 마지막으로 하는 LIS 길이
for i in range(len(A)):
    dp[i] = 1
    for j in range (i):
        if(A[j] < A[i]):
            dp[i] = max(dp[i],dp[j] + 1)
    ret = max(ret, dp[i])

print(ret)