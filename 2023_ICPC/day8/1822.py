# 차집합 구하기
# 집합 A에는 속하면서 집합 B에는 속하지 않는 모든 원소

nA, nB = map(int, input().split())
a = set((map(int, input().split())))
b = set(map(int, input().split()))

result = a - b
if (len(result) == 0):
    print(0)
else:
    print(len(result))
    sortResult = sorted(result)
    for i in sortResult:
        print(i, end=" ")