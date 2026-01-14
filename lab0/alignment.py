"""
Author: Declan Reed
Creation Date: 1/9/26

Alignment Code
"""

print('Hello and welcome to DNA alignment program!')

sequence1 = input("Please enter DNA sequence (using uppercase letters A, T, C, G, and an indel symbol): ")
sequence2 = input("Please enter DNA sequence (using uppercase letters A, T, C, G, and an indel symbol): ")
min_seq = sequence1

if (len(sequence2) < len(sequence1)):
    min_seq = sequence2

print("You entered: \n" + sequence1 + '\n' + sequence2)

command = 'a'
while (command != 'q'):
    command = ''
    if (command == 'u'):
        sequence1 = input("Please enter DNA sequence (using uppercase letters A, T, C, G, and an indel symbol): ")
        sequence2 = input("Please enter DNA sequence (using uppercase letters A, T, C, G, and an indel symbol): ")
        min_seq = sequence1

        if (len(sequence2) < len(sequence1)):
            min_seq = sequence2
    elif (command == 's'):
        matches = 0
        if (len(sequence2) < len(sequence1)):
            min_seq = sequence2
        n = 0
        while (n < len(min_seq)):
            if (sequence1[n:n+1] == sequence2[n:n+1]):
                matches +=1
            n += 1

        print(str(matches) + ' matches found between ' + sequence1 + ' and ' + sequence2)

print("Thank you! Goodbye!")
