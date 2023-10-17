genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

_dict = {k: [] for k in set(genres)}
plays_sum = {k: 0 for k in set(genres)}

for i in range(len(plays)):
  _dict[genres[i]].append([i, plays[i]])

# 2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
for k in _dict.keys():
  _dict[k] = sorted(_dict[k], reverse=True, key=lambda x: (x[1], -x[0]))
  for v in range(len(_dict[k])):
    plays_sum[k] += _dict[k][v][1]

# 1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
sort_plays_sum = sorted(plays_sum.items(), reverse=True, key=lambda x: x[1])

answer = []
for k in sort_plays_sum:
  # 슬라이싱 : 연속적인 객체들에(예: 리스트, 튜플, 문자열) 범위를 지정해 선택해서 객체들을 가져오는 방법 및 표기법
  # start: 슬라이싱을 시작할 시작위치
  # end: 슬라이싱을 끝낼 위치로 end는 포함하지 않음
  top_two_song = sorted(_dict[k[0]], reverse=True, key=lambda x: x[1])[:2]
  for v in top_two_song:
    answer.append(v[0])