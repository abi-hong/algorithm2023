n = int(input())

'''
1) '('일 경우, stack에 넣기
2) ')'일 경우, stack 원소 꺼내서 '('인지 확인
3) 이걸 다 통과하고 스택에 원소가 있을 경우, 짝이 맞지 않은 경우이기에 'NO' 출력
'''

for _ in range(n):
  vps = input()

  stack = []
  for i in vps:
    if (i == '('):
      stack.append(i)
    elif (i == ')'):
      if stack: # 스택에는 '(' 밖에 없다!!
        stack.pop()
      else:
        print('NO')
        break
  else: # for-else문의 else는 break문이 실행되면 실행되지 않는다.
    if stack:
      print('NO')
    else:
      print('YES')