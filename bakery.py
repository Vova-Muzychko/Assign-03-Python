# Copyright 2026 Vova M
# Bakery Croissant Calculator

print("============================================================")
print("Welcome to the Bakery Croissant Calculator!")
print("============================================================")

print("Each croissant costs $2.55")
print("HST is 13% if you buy fewer than 6 croissants.")

# Get input from the user
quantity = float(input("How many croissants do you want? "))

# Set prices
price = 2.55
tax_rate = 0.13

# Check if the input is valid
if quantity <= 0:
    print("Please enter a positive number.")

else:
    # Calculate subtotal
    subtotal = quantity * price

    # Check if HST is needed
    if quantity < 6:
        tax = subtotal * tax_rate
    else:
        tax = 0

    # Calculate total
    total = subtotal + tax

    # Display results
    print("--------------------------------")
    print("Subtotal: $", format(subtotal, ".2f"))
    print("Tax: $", format(tax, ".2f"))
    print("Total cost: $", format(total, ".2f"))
    print("--------------------------------")
