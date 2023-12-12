# display the title as ASCII Art
print("""
                                
                ┌───────────────────────────────────────────────────────────┐ 
                │  ╦  ╦ ╔═╗ ╔╗╔ ╔╦╗ ╦ ╔╗╔ ╔═╗    ╔╦╗ ╔═╗ ╔═╗ ╦ ╦ ╦ ╔╗╔ ╔═╗  │ 
                │  ╚╗╔╝ ║╣  ║║║  ║║ ║ ║║║ ║ ╦    ║║║ ╠═╣ ║   ╠═╣ ║ ║║║ ║╣   │ 
                │   ╚╝  ╚═╝ ╝╚╝ ═╩╝ ╩ ╝╚╝ ╚═╝    ╩ ╩ ╩ ╩ ╚═╝ ╩ ╩ ╩ ╝╚╝ ╚═╝  │  
                └───────────────────────────────────────────────────────────┘
""")

# welcome message [[print("Welcome to name!")]]
print("                                     WELCOME!")

# function that contains menu types (snacks, beverages and desserts)
def menu():
    # list containing 5 snacks stored as dictionaries
    snacks = [
        {"item": "Oman Chips", "code": 71, "price": 3, "stock": 3},
        {"item": "Chocolate Pocky", "code": 72, "price": 2, "stock": 3},
        {"item": "Chunko Cookies", "code": 73, "price": 3.50, "stock": 4},
        {"item": "Cashew Nuts", "code": 74, "price": 2.50, "stock": 2},
        {"item": "Caramel Popcorn", "code": 75, "price": 3, "stock": 2}
    ]
    # list containing 5 beverages stored as dictionaries
    beverages = [
        {"item": "Water bottle", "code": 21, "price": 1.50, "stock": 5},
        {"item": "Sweetened Laban Up", "code": 22, "price": 2.50, "stock": 3},
        {"item": "Iced Tea", "code": 23, "price": 3.50, "stock": 2},
        {"item": "Iced Latte", "code": 24, "price": 4.50, "stock": 4},
        {"item": "Strawberry Milk", "code": 25, "price": 3, "stock": 2}
    ]
    # list containing 5 desserts stored as dictionaries
    desserts = [
        {"item": "Milk Chocolate", "code": 31, "price": 3.50, "stock": 4},
        {"item": "Glazed Donut", "code": 32, "price": 4, "stock": 3},
        {"item": "Brownie", "code": 33, "price": 4.50, "stock": 3},
        {"item": "Chocolate Mousse", "code": 34, "price": 3, "stock": 2},
        {"item": "Vanilla Ice cream", "code": 35, "price": 2.50, "stock": 2}
    ]
    # return the menu lists so that they can be used in the program
    return snacks, beverages, desserts

# function that displays the menu selected as a formatted table
def display_menu(menu_items, menu_type):
    # print the formatted header of the menu selected
    print(f"""
                            ┌──────────────────────────────────────────────────┐
                            │ {menu_type.upper():^48} │
                            ├────┬──────────────────────────┬─────────┬────────┤ 
                            │ #  │ Item                     │ Price   │ Stock  │
                            ├────┼──────────────────────────┼─────────┼────────┤   """)
    # loop through the items of the menu selected
    for item in menu_items:
        # check if any item has no stock
        if item['stock'] == 0: 
            # remove item whose stock is 0
            menu_items.remove(item)
        # print the value of each menu item formatted into the table
        print(f"                            │ {item['code']} │ {item['item']:<24} │ DH {item['price']:.2f} │ {item['stock']:^6} │")
    # print the footer that ends the table
    print("                            └────┴──────────────────────────┴─────────┴────────┘")
