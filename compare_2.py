import pandas as pd

big_df = pd.read_csv('varennes_nrcan_dups.csv')
df = big_df.copy()[:100]
df.to_csv('short.csv', index=False)

tolerance = 3
counter = 0
for feature_index in range(len(df)):
  for next_feature_index in range(feature_index + 1, len(df)):
    a_x = df.iloc[feature_index, 1]
    b_x = df.iloc[next_feature_index + 1, 1]
    subtract_x = a_x - b_x
    print('a_x:', a_x)
    print('b_x:', b_x)
    print('a_x - b_x:', subtract_x)
    print(abs(subtract_x))
    print('-------------------')
    a_y = df.iloc[feature_index, 2]
    b_y = df.iloc[next_feature_index + 1, 2]
    subtract_y = a_y - b_y
    print('a_y:', a_y)
    print('b_y:', b_y)
    print('a_y - b_y:', subtract_y)
    print(abs(subtract_y))
    print('-------------------')
    print('-------------------')
    print('-------------------')

# print(counter)