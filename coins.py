# Count the coins necessary for a specific value and specifies the coins 
# The list coin contains the type of coins (25, 10, 5 and 1 cents)

count = 0
coins = []

# creates a list with the type of coins
coin = [25, 10, 5, 1]

# Enter value
amount = float(input("Enter the amount (U$): "))*100

# function to specify coins
def val_coin():
    for i in range(len(coins)):
        print(f"{coins[i]} of {coin[i]} cents")

# loop to count the total of coins for the amount
for i in coin:
    count = int(amount / i)
    amount = amount - (count * i)
    coins.append(count)
    count = 0

# Show the total of coins for the amount
print(f"Total of coins: {sum(coins)}")

# Show the number of each type of coin
print(val_coin())
