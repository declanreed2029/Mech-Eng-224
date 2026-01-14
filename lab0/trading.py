"""
Author: Declan Reed
Creation Date: 1/9/26

best time to buy and sell code
"""

price_history = input("Enter price history: ")
max = 0
n = 0


while (n < len(price_history)):
    i = n
    while (i < len(price_history)):
        if (int(price_history[i:i+1]) - int(price_history[n:n+1]) > max):
            max = int(price_history[i:i+1]) - int(price_history[n:n+1])
        i += 1
    n += 1

print("Profit: " + str(max))
