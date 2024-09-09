def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * (discount_percent / 100))
        return final_price
    else:
        return price

# Prompts the user to enter the original price and discount percentage
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculates the final price
final_price = calculate_discount(price, discount_percent)

# Prints the final price
if discount_percent >= 20:
    print(f"The final price after applying a {discount_percent}% discount is: ${final_price:.2f}")
else:
    print(f"No discount applied. The original price is: ${price:.2f}")
