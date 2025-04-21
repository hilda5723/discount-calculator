def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    else:
        return price

# Prompt user for input
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call the function and display the result
final_price = calculate_discount(price, discount_percent)

if discount_percent >= 20:
    print(f"Discount applied. Final price: {final_price}")
else:
    print(f"No discount applied. Final price: {final_price}")
