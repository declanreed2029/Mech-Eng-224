"""
Author: Declan Reed
Creation Date: 1/9/26

Score alignment Code
"""

sequence1 = input("Please enter DNA sequence (using uppercase letters A, T, C, G and an indel symbol): ")
sequence2 = input("Please enter DNA sequence (using uppercase letters A, T, C, G and an indel symbol): ")
min_seq = sequence1
n = 0
matches = 0

if (len(sequence2) < len(sequence1)):
    min_seq = sequence2

while (n < len(min_seq)):
    if (sequence1[n:n+1] == sequence2[n:n+1]):
        matches +=1
    n += 1

if (matches == 1):
    print(str(matches) + ' match found between ' + sequence1 + ' and ' + sequence2)
else:
    print(str(matches) + ' matches found between ' + sequence1 + ' and ' + sequence2)
