# (x1, y1)부터 (x2, y2)까지 합
import sys
input =  sys.stdin.readline

n, m = map(int, input().split())

arr = []
for i in range(n):
    a = list(map(int, input().split()))
    arr.append(a)

dp = [[0]*(n+1) for i in range(n+1)] #2차원 배열 선언
'''
[     0  1  2  3  4
   0 [0, 0, 0, 0, 0],
   1 [0, 1, 2, 3, 4],
   2 [0, 2, 3, 4, 5],
   3 [0, 3, 4, 5, 6],
   4 [0, 4, 5, 6, 7],
]
[     0  1  2  3  4
   0 [0, 0, 0, 0, 0],
   1 [0, 0, 0, 0, 0],
   2 [0, 0, 0, 0, 0],
   3 [0, 0, x, 0, 0],
   4 [0, 0, 0, 0, 0],
]
'''

# N개의 줄에는 표에 채워져 있는 수가 1행부터 차례대로 주어진다.
for i in range(1, n+1):
     for j in range(1, n+1):
           dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + arr[i-1][j-1]

# M개의 줄에는 네 개의 정수 x1, y1, x2, y2 가 주어진다.
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    #print('x1', x1, 'y1', y1, 'x2', x2, 'y2', y2)
    print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])

