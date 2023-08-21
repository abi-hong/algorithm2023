n = int(input())
a = list(map(int, input().split()))
#set 사용시, a = set(list(map(int, input().split())))
m = int(input())
b = list(map(int, input().split()))

# set 함수로 중복 제거 -> 정렬까지 함
# 리스트에 특정 값이 있는지 없는지 체크
'''
for num in b:
    if num in a:
        print(1)
    else:
        print(0)
'''

## 이분탐색 사용해보기
a.sort()

for num in b:
    start = 0
    end = n - 1
    isExist = False

    while start <= end:
        mid = (start + end) // 2
        if (num == a[mid]):
            isExist = True
            print(1)
            break
        elif num > a[mid]:
            start = mid + 1
        else:
            end = mid - 1

    if not isExist:
        print(0)