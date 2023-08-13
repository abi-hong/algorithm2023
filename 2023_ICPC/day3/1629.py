A, B, C = map(int, input().split())

def fpow(a, x):
    if (x == 0):
        return 1
    ret = fpow(a, x//2)
    ret = ret * ret % C
    if(x % 2):
        ret = ret * a % C
    return ret

print(fpow(A, B))