from tabulate import tabulate


"""
    - *Display inventory*
    - *Add item*
    - *Remove item*
    - *Update item*
    - *Check low stock*
    - *Exit*

    # Bonus
    - *Buy*
    - *Add sock*
"""

# Multi dimensional array/ List
item_list = [
    {"id": 1, "name": "Revell Condor Airbus A320", "price": 25.0, "quantity": 25},
    {"id": 2, "name": "GeminiJets Airport Terminal Set 1/400 Scale", "price": 28.0, "quantity": 9},
    {"id": 3, "name": "GeminiJets 1/400 Scale Airport Mat", "price": 28.0, "quantity": 9},
    {"id": 4, "name": "Herpa Antonov Airlines AN-225 1/500 Scale", "price": 28.0, "quantity": 9},
    {"id": 5, "name": "JetHut All Nippon Airways 787-9 Dreamliner JA873A (R2-D2 SW) 1/400 Scale", "price": 28.0, "quantity": 9},
    {"id": 6, "name": "JC Wings EasyJet Airbus A321neo G-UZME 1/400 Scale", "price": 28.0, "quantity": 9},
    {"id": 7, "name": "Phoenix Virgin Atlantic Boeing 787-9 G-VBOW 1/400", "price": 28.0, "quantity": 9},
]

next_id = 8  # For auto-generating IDs


def manage_inventory():
    """Main function to manage the inventory system"""
    while True:
        print(
            """
    ==================================================
    Welcome to My Inventory Management System!
    1. List items
    2. Add item
    3. Update item
    4. Delete item
    5. List low stocks
    6. Buy item (Bonus)
    7. Add stock (Bonus)
    8. Exit
        """
        )

        try:
            action = int(input("Enter 1-8 to perform desired function: "))
            
            if action == 1:
                list_items()
            elif action == 2:
                add_item()
            elif action == 3:
                update_item()
            elif action == 4:
                delete_item()
            elif action == 5:
                check_stocks()
            elif action == 6:
                buy_item()
            elif action == 7:
                add_stock()
            elif action == 8:
                print("Thank you for using the Inventory Management System!")
                break
            else:
                print("Invalid option. Please enter a number between 1-8.")
                
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break


def list_items():
    """
    List all the items in the item_list.
    """
    if not item_list:
        print("Inventory is empty.")
        return
    
    # Prepare data for tabulate with low stock indicator
    table_data = []
    for item in item_list:
        quantity_display = f"{item['quantity']} (Low Stock)" if item['quantity'] < 10 else str(item['quantity'])
        table_data.append([
            item['id'],
            item['name'],
            f"${item['price']:.2f}",
            quantity_display
        ])
    
    headers = ["ID", "Name", "Price", "Quantity"]
    print("\n" + "="*80)
    print("INVENTORY LIST")
    print("="*80)
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
    print("="*80)


def add_item():
    """
    Add an item with the following info: id (automatically generated), name, price, and quantity.
    If an item already exists, return an error.
    """
    print("\n" + "="*50)
    print("ADD NEW ITEM")
    print("="*50)
    
    name = input("Enter item name: ").strip()
    if not name:
        print("Error: Item name cannot be empty.")
        return
    
    # Check if item already exists
    for item in item_list:
        if item['name'].lower() == name.lower():
            print("Error: Item already exists in inventory.")
            return
    
    try:
        price = float(input("Enter item price: $"))
        if price < 0:
            print("Error: Price cannot be negative.")
            return
    except ValueError:
        print("Error: Invalid price format.")
        return
    
    try:
        quantity = int(input("Enter item quantity: "))
        if quantity < 0:
            print("Error: Quantity cannot be negative.")
            return
    except ValueError:
        print("Error: Invalid quantity format.")
        return
    
    # Add item to inventory
    global next_id
    new_item = {
        "id": next_id,
        "name": name,
        "price": price,
        "quantity": quantity
    }
    item_list.append(new_item)
    
    print(f"Item '{name}' added successfully with ID: {next_id}")
    next_id += 1


def update_item():
    """
    Update an item by listing all the items then prompting for an item id to update.
    If the id does not exist, return an error.
    """
    print("\n" + "="*50)
    print("UPDATE ITEM")
    print("="*50)
    
    list_items()
    
    try:
        item_id = int(input("Enter item ID to update: "))
    except ValueError:
        print("Error: Invalid ID format.")
        return
    
    # Find item by ID
    item = None
    for i in item_list:
        if i['id'] == item_id:
            item = i
            break
    
    if item is None:
        print("Error: ID not found.")
        return
    
    print(f"\nUpdating item: {item['name']}")
    print("(Press Enter to keep current value)")
    
    # Update name
    new_name = input(f"Current name: {item['name']}\nNew name: ").strip()
    if new_name:
        # Check if new name already exists (excluding current item)
        for other_item in item_list:
            if other_item['id'] != item_id and other_item['name'].lower() == new_name.lower():
                print("Error: Item name already exists.")
                return
        item['name'] = new_name
    
    # Update price
    new_price = input(f"Current price: ${item['price']:.2f}\nNew price: $").strip()
    if new_price:
        try:
            price = float(new_price)
            if price < 0:
                print("Error: Price cannot be negative.")
                return
            item['price'] = price
        except ValueError:
            print("Error: Invalid price format.")
            return
    
    # Update quantity
    new_quantity = input(f"Current quantity: {item['quantity']}\nNew quantity: ").strip()
    if new_quantity:
        try:
            quantity = int(new_quantity)
            if quantity < 0:
                print("Error: Quantity cannot be negative.")
                return
            item['quantity'] = quantity
        except ValueError:
            print("Error: Invalid quantity format.")
            return
    
    print(f"Item updated successfully!")


def delete_item():
    """
    Delete an item by listing all the items then prompting for an item id to delete.
    If the id does not exist, return an error.
    """
    print("\n" + "="*50)
    print("DELETE ITEM")
    print("="*50)
    
    list_items()
    
    try:
        item_id = int(input("Enter item ID to delete: "))
    except ValueError:
        print("Error: Invalid ID format.")
        return
    
    # Find and remove item by ID
    for i, item in enumerate(item_list):
        if item['id'] == item_id:
            item_name = item['name']
            del item_list[i]
            print(f"Item '{item_name}' deleted successfully!")
            return
    
    print("Error: ID not found.")


def check_stocks():
    """
    Displays all items which stocks are less than 10.
    """
    print("\n" + "="*50)
    print("LOW STOCK ITEMS")
    print("="*50)
    
    low_stock_items = [item for item in item_list if item['quantity'] < 10]
    
    if not low_stock_items:
        print("No low-stock items found.")
        return
    
    table_data = []
    for item in low_stock_items:
        table_data.append([
            item['id'],
            item['name'],
            f"${item['price']:.2f}",
            item['quantity']
        ])
    
    headers = ["ID", "Name", "Price", "Quantity"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))


# =========================== Bonus Function =========================== #
def buy_item():
    """
    Displays all the items and their information.
    Prompt for an item id then the quantity that they want to buy.
    If the requested quantity is greater than the available stocks, return an error.
    """
    print("\n" + "="*50)
    print("BUY ITEM")
    print("="*50)
    
    list_items()
    
    try:
        item_id = int(input("Enter item ID to buy: "))
    except ValueError:
        print("Error: Invalid ID format.")
        return
    
    # Find item by ID
    item = None
    for i in item_list:
        if i['id'] == item_id:
            item = i
            break
    
    if item is None:
        print("Error: ID not found.")
        return
    
    try:
        buy_quantity = int(input(f"How many '{item['name']}' do you want to buy? "))
        if buy_quantity <= 0:
            print("Error: Quantity must be positive.")
            return
    except ValueError:
        print("Error: Invalid quantity format.")
        return
    
    if buy_quantity > item['quantity']:
        print(f"Error: Not enough stock. Available: {item['quantity']}")
        return
    
    # Update quantity
    item['quantity'] -= buy_quantity
    total_cost = buy_quantity * item['price']
    
    print(f"Purchase successful!")
    print(f"Bought {buy_quantity} x {item['name']}")
    print(f"Total cost: ${total_cost:.2f}")
    print(f"Remaining stock: {item['quantity']}")


def add_stock():
    """
    Add stock to existing items
    """
    print("\n" + "="*50)
    print("ADD STOCK")
    print("="*50)
    
    list_items()
    
    try:
        item_id = int(input("Enter item ID to add stock: "))
    except ValueError:
        print("Error: Invalid ID format.")
        return
    
    # Find item by ID
    item = None
    for i in item_list:
        if i['id'] == item_id:
            item = i
            break
    
    if item is None:
        print("Error: ID not found.")
        return
    
    try:
        add_quantity = int(input(f"How many '{item['name']}' to add? "))
        if add_quantity <= 0:
            print("Error: Quantity must be positive.")
            return
    except ValueError:
        print("Error: Invalid quantity format.")
        return
    
    # Update quantity
    item['quantity'] += add_quantity
    
    print(f"Stock added successfully!")
    print(f"Added {add_quantity} to {item['name']}")
    print(f"New total stock: {item['quantity']}")


# =========================== Helper Function =========================== #
def helper():
    """
    Calls when in need of simplifying a procedure.
    """
    pass


manage_inventory()
