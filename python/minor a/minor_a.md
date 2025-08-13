# Python Code Problem: Inventory Management System

Create a Python program for a simple inventory management system that allows a user to manage a store's inventory. The program should include the following functionality:

1. Make a python file named `minor_a.py`.
2. Create a function called `manage_inventory()` that serves as the main program.
3. Use a dictionary to store inventory items, where each item has an id(int), name(str), price(float), and quantity(int).
4. Display a menu with the following options:
    - *Display inventory*
    - *Add item*
    - *Remove item*
    - *Update item*
    - *Check low stock*
    - *Exit*

5. Prompt the user to input a choice (1-5) and use conditionals to handle each option:
    - *Display inventory*: Show all items using their id, name, price, and quantities.
    - *Add item:* Prompt for an item name, price and quantity. If the item exists, returns an error saying the item already exists.
    - *Update item*: Prompt for an item id to update. If the item does not exists, return an ID not found error. If the prompt is empty (None), return an error then prompt the same question again.
    - *Remove item*: Prompt for an item id to remove. If the item does not exists, return an ID not found error.
    - *Check low stock*: List all items with a quantity less than 10, or indicate if there are no low-stock items.
    - *Exit*: Terminate the program.

6. Use a loop to keep the program running until the user chooses to exit.
7. Include error handling for invalid inputs (e.g., non-existent items).
8. Use print statements to display the menu, results, and error messages.

## Bonus Points

1. *Buy Option:* Prompt for an item id, then prompt for the amount that the user want to buy. If the prompted quantity is greater than the stock, return an error.

1. *Add Stock Option:* Prompt for an item id, then prompt for the amount of item that the user wants to add.

2. *Advance Update Prompt:* during update (option 3) prompt section, if the user inputs a blank, return the origin value of the prompted data.

3. *Advance List Item Display: * during list items (option 1), if the item's quantity is less than 10, include a message "Low Stock" in the quantity section.

4. *Advance List Item Table Display* use the tabulate python library using `pip install tabulate` in the terminal to beautify the display of items.

> The program should use variables, input, conditionals, a dictionary (collection), loops for iteration, and a function to organize the code.