#!/usr/bin/env python3
message = 'i та і'
count = {}
for character in message:
 count.setdefault(character, 0)
 count[character]+=1
print(count)
