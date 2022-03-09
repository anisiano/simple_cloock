seconds = input("enter second :")
minute = input("enter minute :")
hours = input("enter hours :")
import time
from turtle import *
setup()
tl=Turtle()
while True:
    tl.write(str(hours).zfill(2) + ":" + str(minute).zfill(2) + ":" + str(seconds).zfill(2), font=("arial", 25, "normal")), bgcolor("red")
seconds = seconds + 1
time.sleep(1)
if seconds == 60:
        sedond=0
        minute = minute + 1
if minute == 60:
        minute=0
        houres = hours + 1
