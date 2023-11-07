def solution(priorities, location):
    answer = 0
    while (len(priorities) != 0):
        maxProcess = max(priorities)
        process = priorities[0]
        priorities.pop(0)
        location -= 1
        if (process != maxProcess):
            priorities.append(process)
            if (location < 0):
                location = len(priorities) - 1
        else:
            answer += 1
            if (location < 0):
                break
    return answer