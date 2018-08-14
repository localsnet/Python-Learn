#!/usr/bin/python3
guests=['dima','misha','andrey r']
# Adding new guests
guests.insert(0,'prokofiy')
guests.insert(2,'sasha')
guests.append('vova')
print(guests)
for guest in guests:
 print("Dear friend "+ guest.title()+" My bigger table still not arrive, so I can invite only 2 people")
#Use pop() with while
while len(guests)>2:
 print("Dear friend "+ guests.pop()+" My bigger table still not arrive, sorry I can't invite you")

#Message to existed people
for guest in guests:
 print("Dear friend "+ guest.title()+" Fortunately, you still invited :)")

#Use del to remove all existed

# with LOOP, need some Reverse like in follow manual operations
#for i in range(len(guests)):
# print(i)
# del guests[i]
#print(guests)


del guests[1]
del guests[0]
print(guests)
