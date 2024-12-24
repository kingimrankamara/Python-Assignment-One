def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    
    Parameters:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage to apply.
    
    Returns:
        float: The final price after applying the discount, or the original price if the discount is less than 20%.
    """
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price

# Prompt the user to enter the original price and discount percentage
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price using the calculate_discount function
    final_price = calculate_discount(original_price, discount_percent)

    # Print the result
    if discount_percent >= 20:
        print(f"The final price after applying the discount is: {final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: {original_price:.2f}")
except ValueError:
    print("Please enter valid numeric values for price and discount percentage.")
