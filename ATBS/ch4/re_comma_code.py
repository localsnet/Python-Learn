#!/usr/bin/python3 
#Serj
spam = ['apples', 'bananas', 'tofu', 'cats']

def conver(list_val):
 str_val=''
 list_val.insert(-1,'and')
 for i in range(len(list_val)):
  str_val+=list_val[i]+', '
 last_li=len(list_val[-1])
 sum_str=len(str_val)
 dif_str=sum_str - last_li - 4
 new_str=str_val[:dif_str] + ' '+ str(list_val[-1])
 print(new_str)
 
conver(spam)
