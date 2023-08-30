import heapq
import sys
input =  sys.stdin.readline

# 최대힙 : 부모 노드는 자식 노드보다 작지만 않으면 됨 + 완전이진트리
# python에서 부호를 변경하는 방법을 사용해 최대힙 구현

# 1. 배열에 자연수 x를 넣는다.
# 2. 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
n = int(input())

heap = []
for _ in range(n):
    num = int(input())
    if (num == 0):
        if (len(heap) == 0):
            print(0)
        else:
            # 가장 큰 값을 출력하고 제거
            print(-heapq.heappop(heap))
    else:
        # 배열에 x라는 값을 넣는 연산
        heapq.heappush(heap, -num)

