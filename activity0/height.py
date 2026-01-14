# height.py - A program to convert height in feet and inches into inches
# Declan Reed
# Jan 8th, 2026

feet = int(input('Please enter the number of feet:'))
inches = int(input('Please enter the number of inches:'))
total_inches = feet * 12 + inches
print('Height in inches:', total_inches)
total_cm = total_inches * 2.54
print('Height in centimeters:', total_cm)
