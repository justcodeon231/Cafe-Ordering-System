# Define the menu with prices
menu = {
    "Coffee": 15.00,
    "Sandwich": 30.00,
    "Salad": 25.00,
    "Juice": 10.00,
    "Muffin": 20.00,
    "Pizza Slice": 35.00,
    "Soup": 18.00,
    "Burger": 40.00
}

# Discount threshold and percentage
DISCOUNT_THRESHOLD = 100.00
DISCOUNT_PERCENTAGE = 10.00

def calculate_total_bill(orders):
    total = 0
    for item in orders:
        total += menu[item]
    return total

def apply_discount(total):
    if total > DISCOUNT_THRESHOLD:
        return total - (total * DISCOUNT_PERCENTAGE / 100)
    return total

def write_to_file(name, surname, total):
    with open("cafeteria_orders.txt", "a") as file:
        file.write(f"Customer: {name} {surname}, Total Bill: R{total:.2f}\n")

# Start the program
def main():
    # Input customer details
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    
    # Display menu
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: R{price:.2f}")
    
    # Input number of items ordered
    num_items = int(input("How many items are you ordering? "))
    
    # Collect item names based on the number of orders
    orders = []
    for i in range(num_items):
        item = input(f"Enter item {i+1} from the menu: ")
        while item not in menu:
            print("Item not on the menu. Please select a valid item.")
            item = input(f"Enter item {i+1} from the menu: ")
        orders.append(item)
    
    # Calculate the total bill
    total = calculate_total_bill(orders)
    
    # Apply discount if applicable
    total_with_discount = apply_discount(total)
    
    # Display the total and any discount applied
    if total != total_with_discount:
        print(f"Discount applied! You saved R{total - total_with_discount:.2f}")
    print(f"Total Bill: R{total_with_discount:.2f}")
    
    # Write the customer details and total bill to a file
    write_to_file(name, surname, total_with_discount)
    print("Thank you for your order! Your details have been saved.")
    # print(orders)

# Run the program
if __name__ == "__main__":
    main()
