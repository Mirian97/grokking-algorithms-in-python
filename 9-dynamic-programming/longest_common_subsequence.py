dp_fosh_table = ["f", "o", "s", "h"]
dp_fish_table = ["f", "i", "s", "h"]

dp_table = [[0 for i in range(len(dp_fosh_table))] for i in range(len(dp_fish_table))]

for i in range(0, len(dp_fosh_table)):
  for j in range(0, len(dp_fish_table)):
    if dp_fish_table[j] == dp_fosh_table[i]:
      dp_table[i][j] = dp_table[i-1][j-1] + 1
    else:
      dp_table[i][j] = max(dp_table[i-1][j], dp_table[i][j-1])
      
for i in dp_table:
  print(i)