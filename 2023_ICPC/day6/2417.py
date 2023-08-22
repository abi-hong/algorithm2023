n = int(input())
#정수가 주어지면, 그 수의 정수 제곱근을 구하는 프로그램을 작성하시오.
#첫째 줄에 q2 ≥ n인 가장 작은 음이 아닌 정수 q를 출력한다. -> 정수형으로 올림해서 출력해야 한다.
start = 0
end = n
while start <= end:
    mid = (start + end) // 2
    if mid ** 2 < n:
        start = mid + 1
    else:
        end = mid - 1
print(start)