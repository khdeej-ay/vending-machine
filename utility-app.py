# Utility App | VENDING MACHINE

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

# list containing 5 snacks stored as dictionaries
snacks = [
    {"item": "Takis Fuego Crisps", "code": 71, "price": 4, "stock": 3},
    {"item": "Chocolate Pocky", "code": 72, "price": 2, "stock": 3},
    {"item": "Mozzarella String Cheese", "code": 74, "price": 2.50, "stock": 2},
    {"item": "Caramel Popcorn", "code": 75, "price": 3, "stock": 2},
    {"item": "Chocolate Chunkos", "code": 73, "price": 3.50, "stock": 4}
]
# list containing 5 beverages stored as dictionaries
beverages = [
    {"item": "Water bottle", "code": 21, "price": 1.50, "stock": 5},
    {"item": "Pineapple Juice", "code": 22, "price": 2.50, "stock": 2},
    {"item": "Brown Sugar Milk Tea", "code": 23, "price": 3.50, "stock": 3},
    {"item": "Caramel Macchiato", "code": 24, "price": 4.50, "stock": 4},
    {"item": "Strawberry Milkshake", "code": 25, "price": 3, "stock": 2}
]
# list containing 5 desserts stored as dictionaries
desserts = [
    {"item": "Hazelnut Chocolate", "code": 31, "price": 3.50, "stock": 4},
    {"item": "Plain Glazed Donut", "code": 32, "price": 4, "stock": 3},
    {"item": "Caramel Fudge Brownie", "code": 33, "price": 4.50, "stock": 3},
    {"item": "Chocolate Mousse", "code": 34, "price": 3, "stock": 2},
    {"item": "Salted Caramel Ice cream", "code": 35, "price": 2.50, "stock": 2}
]

def menu_choice():
    global menu_selected
    while True: 
        choice = input("\nTYPE 1 FOR SNACKS, 2 FOR BEVERAGES, 3 FOR DESSERTS, OR 0 TO QUIT: ").strip()
        if choice == "0":            
            break        
        elif choice == "1":            
            display_menu(snacks, "Snacks")
            print("\nCHOOSE AN ITEM")                    
            menu_selected = snacks          
            break  
        elif choice == "2": 
            display_menu(beverages, "Beverages")
            print("\nCHOOSE AN ITEM")        
            menu_selected = beverages
            break
        elif choice == "3": 
            display_menu(desserts, "Desserts")
            print("\nCHOOSE AN ITEM")        
            menu_selected = desserts
            break
        else: 
            print("\n                                              Incorrect choice. Please try again. ")
            continue

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