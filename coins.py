count = 0
coins = []

# Enter value
amount = float(input("Enter the amount (U$): "))*100

# creates a list with the coins
coin = [25, 10, 5, 1]

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
