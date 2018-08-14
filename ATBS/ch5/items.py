#!/usr/bin/env python3
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
'Bob': {'ham sandwiches': 3, 'apples': 2},
'Carol': {'cups': 3, 'apple pies': 1}}
print('{', end='')
for k, v in allGuests.items():
  print(k + str(v))
print('}',end='')

