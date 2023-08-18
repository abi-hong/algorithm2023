t = int(input())

# 초기조건 : dp[0] = 첫번째 배열 원소
# dp[i] = max(dp[i-1] + x[i], x[i])
# dp[i] := i번쩨 원소까지의 부분배열 중 가장 큰 각 원소의 합

for _ in range(t):
    n = int(input())
    x = list(map(int, input().split()))

    dp = [0]*n
    dp[0] = x[0]
    for j in range(1, n):
        dp[j] = max(dp[j-1]+x[j], x[j])    
         
    print(max(dp))
