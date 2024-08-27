a = list(range(5, 0, -1))

print(a)

for each in range(len(a)):
  for every in range(each + 1, len(a)):
    print(each)
    print(every)
    print(f'{a[each]} - {a[every]} = ', a[each] - a[every])
    print('----------------------')
  print('----------------------')