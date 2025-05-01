dp_hish_table = ["h", "i", "s", "h"]
dp_fish_table = ["f", "i", "s", "h"]

dp_table = [[0 for i in range(len(dp_hish_table))] for i in range(len(dp_fish_table))]

for i in range(0, len(dp_fish_table)):
  for j in range(0, len(dp_hish_table)):
    if dp_fish_table[j] == dp_hish_table[i]:
      dp_table[i][j] = dp_table[i-1][j-1] + 1
    else:
      dp_table[i][j] = 0
      
for i in dp_table:
  print(i)