# Takes a credit card number and returns it's American Express, Mastercard or Visa
# Also checks the number with the Luhn's Algorithm

# Specifications for each brand
len_card = {"amex":15, "master":16, "visa":(13, 16)}
card_init = {"American Express":("34", "37"), "Mastercard":("51", "52", "53", "54", "55"), "Visa":("4")}

card_number2 = []
numbers = []
numbers_double = []

card_number = input("Enter card number to check if it's valid (only numbers, no spaces): ")

# Checks users entry
def valid_entry():
    global card_number
    if card_number.isdigit() == False:
        card_number = input("Enter card number (only numbers, no spaces): ")
        valid_entry()

# Checks what brand
def card_brand():
    for i in len_card:
        if len(card_number) == len_card[i]:
            for j in card_init:
                if card_number.startswith(card_init[j]):
                    print(f"{j} valid card")

valid_entry()

# Checks if it is compatible with Luhn's Algorithm
count = 0
card_number2 = reversed(card_number)
card_number2 = list(map(lambda x: int(x), card_number2))

# This loop separates in 2 lists
for i in card_number2:
    if count % 2 == 0:
        numbers.append(i)
    else:
        numbers_double.append(i)
    count += 1

# double numbers before sum
numbers_double = list(map(lambda x: (x) * 2, numbers_double))

# turns to string again to separe 2 digits numbers before sum
for i in numbers_double:
    numbers_double = list(map(lambda x: str(x), numbers_double))
    numbers_double = "".join(numbers_double)

# turns to intergers again to do the final sum
for i in numbers_double:
    numbers_double = list(map(lambda x: int(x), numbers_double))
final_number = sum(numbers) + sum(numbers_double)

# Checks if the sum ends with zero and validate the card number with the specific brandb
if final_number % 10 == 0:
    card_brand()
else:
    print("Invalid card")

