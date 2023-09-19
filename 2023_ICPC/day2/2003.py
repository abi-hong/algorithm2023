# i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수

n, m = map(int, input().split())
a = list(map(int, input().split()))

start = 0
end = 0
interval_sum = 0
result = 0

for start in range(n):
  while (interval_sum < m) and (end < n):
    interval_sum += a[end]
    end += 1
  if (interval_sum == m):
    result += 1
  interval_sum -= a[start]
  
print(result)