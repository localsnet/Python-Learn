#!/usr/bin/python
class Rectangle:
 
    def __init__(iself, x, y):
        iself.x = x
        iself.y = y
 
    description = "This rectangle have not description yet"
    author = "This rectangle have not author yet"
 
    def area(iself):
# Area
        return iself.x * iself.y
 
    def perimeter(iself):
# Perimeter
        return 2 * iself.x + 2 * iself.y
 
    def describe(iself, text):
#  
        iself.description = text
 
    def authorName(iself, text):
#  
        iself.author = text
 
    def scaleSize(iself, scale):
        iself.x = iself.x * scale
        iself.y = iself.y * scale

my_rect = Rectangle(2, 3)


print my_rect.area()

print my_rect.perimeter()

my_rect.describe(u"It's a big rectangle")

my_rect.scaleSize(0.5)

print my_rect.area()


