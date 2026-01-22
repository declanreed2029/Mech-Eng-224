"""
Author: Declan Reed
Creation Date: 1/9/26

Speeding ticket code
"""

speed_limit = int(input())
driving_speed = int(input())
ticket = 0

if ((driving_speed - speed_limit < 6) and (speed_limit - driving_speed < 10)):
    ticket = 0
elif (speed_limit - driving_speed >= 10):
    ticket = 50
elif (driving_speed - speed_limit > 40):
    ticket = 300
elif (driving_speed - speed_limit > 20):
    ticket = 150
elif (driving_speed - speed_limit >= 6):
    ticket = 75

print(str(ticket))
