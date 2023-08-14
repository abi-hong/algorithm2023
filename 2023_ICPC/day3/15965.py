import math
n = 10**7
k = int(input())

findPrime = [True for i in range(n+1)]
prime = []

for i in range(2, n + 1):
    if findPrime[i]:
        prime.append(i)
        for j in range(i+i, n+1, i):
            findPrime[j] = False
        '''
        j = 2
        while i * j <= n: # 소수인 수의 배수들은 다 False 처리
            findPrime[i*j] = False
            j += 1
        '''

print(prime[k-1])

