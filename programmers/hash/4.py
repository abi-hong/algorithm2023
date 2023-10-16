def solution(clothes):
    answer = 1

    # dictionary 만들기
    _dict = {k: [] for _, k in clothes}

    # dictionary에 값 넣기
    for v, k in clothes:
        _dict[k].append(v)

    # 가능한 조합의 개수
    '''
    (빨간바지, 파란바지, 투명바지), (빨간옷, 파란옷, 투명옷)
    가능한 조합의 개수 = 3 * 3 - 1
    '''
    for v in _dict.values():
        answer *= (len(v) + 1)
    answer -= 1
    return answer