"""
Author: Declan Reed
Creation Date: 1/9/26

Count text input length code
"""

text = input()
index = 0
char_amt = 0

while index < len(text):
    if (text[index: index + 1] != " ") and (text[index: index + 1] != ".") and (text[index: index + 1] != "!") and (text[index: index + 1] != ","):
        char_amt += 1
    index += 1

print(char_amt)
