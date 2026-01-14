"""
Author: Declan Reed
Creation Date: 1/9/26

Heating and cooling days code
"""
temp = 0
heating_days = 0
cooling_days = 0

while temp >= -459:
    temp_today = int(input("Enter the average daily temperature: "))
    if (temp_today < 60) and (temp_today >= -459):
        heating_days += 1
    elif temp_today > 80:
        cooling_days += 1
    temp = temp_today

print("Heating days: " + str(heating_days))
print("Cooling days: " + str(cooling_days))
