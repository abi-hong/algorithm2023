import sys

c = [list(map(int, input().split())) for _ in range(5)]
mc = []
for _ in range(5):
    mc += list(map(int, input().split()))

def check():
   bingo = 0
   # 가로 줄 확인
   for x in c:
      if (x.count(0) == 5):
         bingo += 1
   
   # 세로 줄 확인
   for y in range(5):
      countY = 0
      for x in range(5):
         if (c[x][y] == 0):
            countY += 1
      if (countY == 5):
         bingo += 1
   
   # 가로 위 시작 대각선 확인
   countLeft = 0
   for i in range(5):
      if (c[i][i] == 0):
         countLeft += 1
   if (countLeft == 5):
    bingo += 1
   
   # 가로 위 시작 대각선 확인
   countRight = 0
   for i in range(5):
      if (c[i][4 - i] == 0):
         countRight += 1
   if (countRight == 5):
    bingo += 1

   return bingo
    

      
cnt = 0
for i in range(25):
  for x in range(5):
     for y in range(5):
        if (c[x][y] == mc[i]):
           c[x][y] = 0
           cnt += 1

  if (cnt >= 12):
   # 빙고 있는지 확인
   result = check()
   if (result >= 3):
     # 첫째 줄에 사회자가 몇 번째 수를 부른 후 철수가 "빙고"를 외치게 되는지 출력
     print(i + 1)
     break