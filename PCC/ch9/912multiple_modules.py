#!/usr/bin/python3
from privadmin import Admin
#Instance1
user1 = Admin('John', 'Doe')

user1.specify_opt(33,'male')
user1.privileg.privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]  
user1.greet_user()
user1.describe_user()
user1.privileg.show_privileges()
