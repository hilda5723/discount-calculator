# discount-calculator
Python function to apply discounts based on percentage.
# 🧮 Discount Calculator

A simple Python script that calculates the final price of an item after applying a discount. If the discount is **20% or more**, the discount is applied; otherwise, the original price remains.

## 🚀 How It Works

- The user is prompted to enter:
  - The original price of the item
  - The discount percentage
- If the discount percentage is 20% or higher, the script applies the discount.
- If it's less than 20%, the original price is returned.

## 🧠 Function Used

```python
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    else:
        return price
