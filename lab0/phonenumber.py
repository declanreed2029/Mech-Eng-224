"""
Author: Declan Reed
Creation Date: 1/9/26

Phone number breakdown Code
"""

phone_number = input("Type phone number unformatted: ")

print('(' + str(phone_number[0:3]) + ') ' + str(phone_number[3:6]) + '-' + str(phone_number[6:]))
