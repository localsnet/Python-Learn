#!/usr/bin/python3
from privileges import Admin

#Instance1
user1 = Admin('John', 'Doe')

user1.specify_opt(33,'male')
user1.privileg.privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
user1.privileg.show_privileges()

