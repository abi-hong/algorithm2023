n, m = map(int, input().split())
a = list(map(int, input().split()))

start = 0
end = 0
interval_sum = 0
count = 0

for start in range(len(a)):
    while(interval_sum < m and end < len(a)):
        interval_sum += a[end]
        end += 1
    if interval_sum == m:
        count += 1
    interval_sum -= a[start]
print(count)