#Write a program that prompts for the user’s favorite number .
import json
filename='favnumber.json'
favnumber=input('Enter your favorite number')
#Use json.dump() to store this number in a file .
with open(filename,'w') as f_obj:
    json.dump(favnumber,f_obj)
