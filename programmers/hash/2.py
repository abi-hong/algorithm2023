# 효율성 통과 못함
'''
def solution(participant, completion):
    for name in completion:
        for result in participant:
            if (name == result):
                participant.remove(result)
                break
    
    answer = participant[0]
    return answer
'''

# 힌트 : 참여한 선수들과 완주한 선수들을 정렬 후 비교하면 어떨까요? 
def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if (completion[i] != participant[i]):
            answer = participant[i]
            break
    else:
        answer = participant[-1]

    return answer


# Counter 생성자는 여러 형태의 데이터를 인자로 받는데요. 
# 먼저 중복된 데이터가 저장된 배열을 인자로 넘기면 각 원소가 몇 번씩 나오는지가 저장된 객체
'''
import collections

answer = collections.Counter(participant) - collections.Counter(completion)
print(list(answer.keys())[0])
'''