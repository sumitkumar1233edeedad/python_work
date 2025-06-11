import numpy as np
"""
Tutorial-based Example: Applying a Percentage Discount to Product Prices Using NumPy
This script demonstrates how to use NumPy for vectorized operations to apply a fixed percentage discount to an array of product prices.
Steps:
1. Define an array of product prices.
2. Specify a discount percentage.
3. Calculate the final prices after applying the discount using broadcasting.
4. Print the discounted prices.
Variables:
- prices (np.ndarray): Array containing the original prices of products.
- discount (float): Discount percentage to be applied to each product.
- finall_prices (np.ndarray): Array containing the final prices after discount.
This example is useful for understanding NumPy broadcasting and basic array arithmetic for financial calculations.
"""

# Define an array of product prices
prices =  np.array([2000, 400, 200, 300, 3000, 6000])

# Set the discount percentage (10%)
discount = 10  # 10% off per product

# Calculate the final prices after applying the discount using broadcasting
final_prices = prices - (prices * (discount / 100))

# Print the discounted prices
print(final_prices)
