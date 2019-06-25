
import datetime


name=input("your name:")
age = int(input("your age:"))
now = datetime.datetime.now()
print("you will turn to 95 in this year:",(now.year-age)+95)

