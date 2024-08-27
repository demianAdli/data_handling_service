import pandas as pd

df = pd.read_csv('varennes_nrcan_dups.csv')
# df = big_df.copy()[:100]
# df.to_csv('short.csv', index=False)

tolerance = 1
counter = 0
centroid_x = df['centroid_x'].tolist()
centroid_y = df['centroid_y'].tolist()
feature_ids = []

for feature_index in range(len(centroid_x)):
  for next_feature_index in range(feature_index + 1, len(centroid_x)):
    a_x = centroid_x[feature_index]
    b_x = centroid_x[next_feature_index]
    subtract_x = a_x - b_x
    a_y = centroid_y[feature_index]
    b_y = centroid_y[next_feature_index]
    subtract_y = a_y - b_y
    if abs(subtract_x) < tolerance and abs(subtract_y) < tolerance:
      counter += 1

print(counter)

