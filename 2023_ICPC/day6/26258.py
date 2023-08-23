n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
# 풍선 m개를 만들기 위해 최소 몇분이 걸릴까
# 3 5 7 

start = a[0] # 최소 시간
end = 1000000 ** 2 # 최대 시간
res = end
while(start <= end):
    mid = (start + end) // 2
    print('mid', mid)
    count = sum([mid // x for x in a])
    print('count', count)
    if count >= m:
        end = mid - 1
        res = min(res, mid)
    elif count < m:
        start = mid + 1
print(res)