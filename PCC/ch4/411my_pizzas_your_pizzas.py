#!/usr/bin/python3
pizzas=['Alando','Santiago','Borimo','Corsica']
for p in pizzas:
 print('I like '+p+' pizza')
print('But really want to go to '+pizzas[1])

#Previous exercise end
friend_pizzas=pizzas[:]
pizzas.append('Montevideo')
friend_pizzas.append('Carribean')

print('\nMy favorite pizzas are:')
for i in pizzas:
 print(i)

print("\nMy friend's favorite pizzas are:")
for i in friend_pizzas:
 print(i)

