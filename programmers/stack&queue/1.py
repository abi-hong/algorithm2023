def solution(arr):
    answer = []
    element = -1
    for i in arr:
        if (element == i):
            continue;
        else:
            element = i
            answer.append(i)
    return answer