"""
Author: Declan Reed
Creation Date: 1/9/26

Alignment Code
"""

print('Hello and welcome to DNA sequence alignment program!')

sequence1 = input("Please enter DNA sequence (using uppercase letters A, T, C, G and an indel symbol): ")
sequence2 = input("Please enter DNA sequence (using uppercase letters A, T, C, G and an indel symbol): ")
min_seq = sequence1

if (len(sequence2) < len(sequence1)):
    min_seq = sequence2

print("You entered: " + sequence1 + '\n' + sequence2)

command = 'a'
while (command != 'q'):
    command = ''
    command = input("Select one of the following commands: 'u' to update sequences \n's' to score the alignment \n'q' to quit\n")
    if (command == 'u'):
        sequence1 = input("Please enter DNA sequence (using uppercase letters A, T, C, G and an indel symbol): ")
        sequence2 = input("Please enter DNA sequence (using uppercase letters A, T, C, G and an indel symbol): ")
        print("You entered: " + sequence1 + '\n' + sequence2)
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

        if ((len(sequence1) == 0) or (len(sequence2) == 0)):
            print('Invalid DNA sequences entered, please re-enter sequences')
        else:
            print(str(matches) + ' matches found between ' + sequence1 + ' and ' + sequence2)
    elif (command == 'q'):
        break

print("Thank you! Goodbye!")
