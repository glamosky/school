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
# See randomizer.py for more details. I also made a helper function inspired by randomizer.py.
item_list = [
    {'id': 1, 'name': 'GeminiJets Boeing 777-300ER Emirates 1/400', 'price': 60, 'quantity': 23},
    {'id': 2, 'name': 'GeminiJets Airbus A350-900 Qatar Airways 1/400', 'price': 60, 'quantity': 22},
    {'id': 3, 'name': 'NG Models Boeing 737-800 American Airlines 1/400', 'price': 40, 'quantity': 40},
    {'id': 4, 'name': 'Phoenix Models Boeing 787-9 All Nippon Airways 1/400', 'price': 20, 'quantity': 48},
    {'id': 5, 'name': 'JC Wings Airbus A321neo easyJet 1/400', 'price': 20, 'quantity': 82},
    {'id': 6, 'name': 'NG Models Boeing 757-200 Delta Air Lines 1/400', 'price': 20, 'quantity': 81},
    {'id': 7, 'name': 'Herpa Boeing 747-400 Lufthansa 1/500', 'price': 20, 'quantity': 21},
    {'id': 8, 'name': 'AeroClassics Airbus A310-300 Air France 1/400', 'price': 40, 'quantity': 29},
    {'id': 9, 'name': 'Phoenix Models Airbus A380-800 Emirates 1/400', 'price': 60, 'quantity': 64},
    {'id': 10, 'name': 'GeminiJets Boeing 767-300ER Japan Airlines 1/400', 'price': 40, 'quantity': 100},
    {'id': 11, 'name': 'NG Models Boeing 787-10 United Airlines 1/400', 'price': 60, 'quantity': 11},
    {'id': 12, 'name': 'JC Wings Airbus A350-1000 British Airways 1/400', 'price': 40, 'quantity': 43},
    {'id': 13, 'name': 'Phoenix Models Airbus A330-300 Cathay Pacific 1/400', 'price': 60, 'quantity': 78},
    {'id': 14, 'name': 'NG Models Boeing 737 MAX 8 Southwest 1/400', 'price': 40, 'quantity': 36},
    {'id': 15, 'name': 'Herpa Airbus A321neo Lufthansa 1/500', 'price': 40, 'quantity': 82},
    {'id': 16, 'name': 'AeroClassics McDonnell Douglas DC-10-30 KLM 1/400', 'price': 60, 'quantity': 53},
    {'id': 17, 'name': 'GeminiJets Boeing 737-700 Southwest Canyon Blue 1/400', 'price': 40, 'quantity': 92},
    {'id': 18, 'name': 'JC Wings Boeing 777-9X Lufthansa 1/400', 'price': 20, 'quantity': 75},
    {'id': 19, 'name': 'GeminiJets Airport Ground Service Set 1/400', 'price': 100, 'quantity': 17},
    {'id': 20, 'name': 'GeminiJets Airport Terminal Set 1/400', 'price': 40, 'quantity': 93},
    {'id': 21, 'name': 'Revell Boeing 747-8 Lufthansa 1/144 Plastic Kit', 'price': 60, 'quantity': 46},
    {'id': 22, 'name': 'Airfix Supermarine Spitfire Mk.IXc 1/48 Plastic Kit', 'price': 100, 'quantity': 54},
    {'id': 23, 'name': 'Tamiya F-16C Block 50 Fighting Falcon 1/48 Plastic Kit', 'price': 100, 'quantity': 24},
    {'id': 24, 'name': 'Hasegawa F-14D Tomcat 1/72 Plastic Kit', 'price': 20, 'quantity': 83},
    {'id': 25, 'name': 'Zvezda Airbus A320neo 1/144 Plastic Kit', 'price': 40, 'quantity': 57},
    {'id': 26, 'name': 'Italeri Lockheed Martin F-35A Lightning II 1/48 Plastic Kit', 'price': 40, 'quantity': 83},
    {'id': 27, 'name': 'Trumpeter Sukhoi Su-27 Flanker B 1/72 Plastic Kit', 'price': 40, 'quantity': 73},
    {'id': 28, 'name': 'Academy Boeing B-17G Flying Fortress 1/72 Plastic Kit', 'price': 60, 'quantity': 16},
    {'id': 29, 'name': 'Eduard Messerschmitt Bf 109G-6 ProfiPACK 1/48 Plastic Kit', 'price': 20, 'quantity': 54},
    {'id': 30, 'name': 'Revell Airbus A380-800 Emirates 1/144 Plastic Kit', 'price': 60, 'quantity': 52},
    {'id': 31, 'name': 'Airfix Hawker Hurricane Mk.I 1/72 Plastic Kit', 'price': 60, 'quantity': 44},
    {'id': 32, 'name': 'Tamiya North American P-51D Mustang 1/48 Plastic Kit', 'price': 20, 'quantity': 31},
    {'id': 33, 'name': 'Hasegawa F/A-18E Super Hornet 1/72 Plastic Kit', 'price': 20, 'quantity': 56},
    {'id': 34, 'name': 'Zvezda Boeing 777-300ER 1/144 Plastic Kit', 'price': 60, 'quantity': 100},
    {'id': 35, 'name': 'Italeri Lockheed C-130H Hercules 1/72 Plastic Kit', 'price': 60, 'quantity': 86},
    {'id': 36, 'name': 'Trumpeter Mikoyan MiG-29 9-13 1/72 Plastic Kit', 'price': 60, 'quantity': 46},
    {'id': 37, 'name': 'Academy SR-71A Blackbird 1/72 Plastic Kit', 'price': 20, 'quantity': 28},
    {'id': 38, 'name': 'Eduard Spitfire Mk.Vb Weekend Edition 1/48 Plastic Kit', 'price': 100, 'quantity': 34},
    {'id': 39, 'name': 'Kinetic F-16I Sufa 1/48 Plastic Kit', 'price': 40, 'quantity': 27},
    {'id': 40, 'name': 'Hobby Boss A-10C Thunderbolt II 1/48 Plastic Kit', 'price': 100, 'quantity': 66},
    {'id': 41, 'name': 'Revell Condor Airbus A320', 'price': 100, 'quantity': 88},
    {'id': 42, 'name': 'GeminiJets Airport Terminal Set 1/400 Scale', 'price': 60, 'quantity': 22},
    {'id': 43, 'name': 'GeminiJets 1/400 Scale Airport Mat', 'price': 60, 'quantity': 13},
    {'id': 44, 'name': 'Herpa Antonov Airlines AN-225 1/500 Scale', 'price': 20, 'quantity': 27},
    {'id': 45, 'name': 'JetHut All Nippon Airways 787-9 Dreamliner JA873A (R2-D2 SW) 1/400 Scale', 'price': 60, 'quantity': 42},
    {'id': 46, 'name': 'JC Wings EasyJet Airbus A321neo G-UZME 1/400 Scale', 'price': 20, 'quantity': 99},
    {'id': 47, 'name': 'Phoenix Virgin Atlantic Boeing 787-9 G-VBOW 1/400', 'price': 100, 'quantity': 55},
    {'id': 48, 'name': 'Icelandair A321neo 1/200', 'price': 40, 'quantity': 21},
    {'id': 49, 'name': 'USAF B-52H 1/400', 'price': 20, 'quantity': 12},
    {'id': 50, 'name': 'Icelandair A321neo 1/200', 'price': 20, 'quantity': 82},
    {'id': 51, 'name': 'Antonov 225 Mriya 1/400', 'price': 40, 'quantity': 45},
    {'id': 52, 'name': 'American Eagle Saab 340B 1/200', 'price': 100, 'quantity': 49},
    {'id': 53, 'name': 'TUI 737 MAX 8 1/200', 'price': 40, 'quantity': 28},
    {'id': 54, 'name': 'Helvetic E190-E2 1/200', 'price': 20, 'quantity': 47},
    {'id': 55, 'name': 'Aerolineas Argentinas 737M8 1/200', 'price': 100, 'quantity': 34},
    {'id': 56, 'name': 'Eastern 727-100 1/200', 'price': 100, 'quantity': 11},
    {'id': 57, 'name': 'jetBlue A321neo 1/200', 'price': 40, 'quantity': 93},
    {'id': 58, 'name': 'US Navy F/A-18C Hornet 1/72', 'price': 100, 'quantity': 59},
    {'id': 59, 'name': 'Pan Am 757-200 1/200', 'price': 40, 'quantity': 91},
    {'id': 60, 'name': 'Pan Am 757-200 1/400', 'price': 40, 'quantity': 100},
    {'id': 61, 'name': 'USAF C-130 Montana ANG 1/200', 'price': 20, 'quantity': 91},
    {'id': 62, 'name': 'Cubana ATR-72 1/200', 'price': 100, 'quantity': 92},
    {'id': 63, 'name': 'United 777-200 Star Alliance 1/400', 'price': 60, 'quantity': 52},
    {'id': 64, 'name': 'British Airways A380 1/400', 'price': 20, 'quantity': 95}
]

next_id = 65  # For auto-generating IDs


def manage_inventory():
    """
    Main function to manage the inventory system
    """
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
    8. Randomize Inventory (Bonus)
    9. Exit
        """
        )

        try:
            action = int(input("Enter 1-9 to perform desired function: "))
            
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
                randomize_inventory()
            elif action == 9:
                print("Thank you for using the Inventory Management System!")
                break
            else:
                print("Invalid option. Please enter a number between 1-9.")
                
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


def randomize_inventory():
    """
    I decided to just write it here instead. Randomize prices and quantities for all items in the inventory.
    This helper function uses the same logic as randomizer.py.
    """
    import random
    
    print("\n" + "="*50)
    print("RANDOMIZE INVENTORY")
    print("="*50)
    
    # prices
    price_choices = [20, 40, 60, 100]
    
    # randomize each item
    for item in item_list:
        item["price"] = random.choice(price_choices)
        item["quantity"] = random.randint(10, 100)
    
    print("Inventory has been randomized!")
    print("All items now have random prices ($20, $40, $60, or $100) and quantities (10-100).")
    print("Use 'List items' to see the updated inventory.")


manage_inventory()






