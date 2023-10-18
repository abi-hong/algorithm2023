array = [1, 5, 2, 6, 3, 7, 4]	
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

answer = []
for command in commands:
  sort_array = sorted(array[command[0] - 1:command[1]])
  answer.append(sort_array[command[2]-1])
print(answer)
