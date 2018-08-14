#!/usr/bin/python3
guests=['dima','misha','andrey r']
#Print using for Loop with missed title method
for guest in guests:
 print("Dear friend "+ guest.title()+", I'd like to invite you to dinner")
# Print a news about bigger table	
for guest in guests:
 print("Dear friend "+ guest.title()+",I found a bigger dinner table.")
# Adding new guests
guests.insert(0,'prokofiy')
guests.insert(2,'sasha')
guests.append('vova')
for guest in guests:
 print("Dear friend "+ guest.title()+", I'd like to invite you to dinner at my bigger table")
print(guests)
