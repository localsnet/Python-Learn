#!/usr/bin/python3
guests=['dima','misha','sasha','andrey r']
print("Dear friend "+ guests[0].title()+", I'd like to invite you to dinner")
print("Dear friend "+ guests[1].title()+", I'd like to invite you to dinner")
print("Dear friend "+ guests[2].title()+", I'd like to invite you to dinner")
print("Dear friend "+ guests[3].title()+", I'd like to invite you to dinner")
#3-4 end and start 3-5
print("My friend "+ guests[2].title()+", can't make a dinner")
# Replace with index
guests[2]='prokofiy'
#Print a second set messages using for Loop with missed title method
for guest in guests:
 print("Dear friend "+ guest.title()+", I'd like to invite you to dinner on a new time, because I've to search for new guest ")


