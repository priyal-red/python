#user/bin/python3

import datetime
name=input("enter your name: ")
now=datetime.datetime.now()

b=now.hour

if b>6 and b<12:
   print("Gud Morning",name)

elif b>12 and b<18:
   print("Gud Afternoon",name)

elif b>18 and b<23:
   print("Gud Evening",name)

else:
   print("Gud night",name)
