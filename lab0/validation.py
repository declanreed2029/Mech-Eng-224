"""
Author: Declan Reed
Creation Date: 1/9/26

DNA validation code
"""

sequence = input("Please enter DNA sequence (using uppercase letters A, T, C, G, and an indel symbol): ")
n = 0
valid = True

while ((n < len(sequence)) and (valid)):
    if (sequence == ''):
        valid = False
    elif ((sequence[n:n+1] != 'A') and (sequence[n:n+1] != 'C') and (sequence[n:n+1] != 'T') and (sequence[n:n+1] != 'G') and (sequence[n:n+1] != '-')):
        valid = False
    n += 1

if (valid):
    print(sequence + ' is a valid DNA sequence')
else:
    print(sequence + ' is not a valid DNA sequence')
