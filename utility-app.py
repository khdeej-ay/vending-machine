### Utility App | VENDING MACHINE

# import the time module (to access the time.sleep function)
import time

# function to use the time.sleep function
def pause():
    # 1-second pause
    time.sleep(1)

def choose_item():
    print("\nCHOOSE AN ITEM")        

def menu_choice():
    global menu_selected
    while True: 
        choice = input("\nTYPE 1 FOR SNACKS, 2 FOR BEVERAGES, 3 FOR DESSERTS, OR 0 TO QUIT: ").strip()
        if choice == "0":            
            break        
        elif choice == "1":            
            display_menu(snacks, "Snacks")
            choose_item()
            menu_selected = snacks          
            break  
        elif choice == "2": 
            display_menu(beverages, "Beverages")
            choose_item()
            menu_selected = beverages
            break
        elif choice == "3": 
            display_menu(desserts, "Desserts")
            choose_item()
            menu_selected = desserts
            break
        else: 
            print("\nIncorrect choice. Please try again. ")
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
    # loop through copy of menu_items to avoid modifying it directly during iteration
    for item in menu_items.copy():
        # check if any item has stock 0 or less
        if item['stock'] <= 0:    
            # remove item with stock 0 or less
            menu_items.remove(item)
        # print the value of each menu item formatted into the table
        print(f"                            │ {item['code']} │ {item['item']:<24} │ DH {item['price']:.2f} │ {item['stock']:^6} │")
    # print the footer that ends the table
    print("                            └────┴──────────────────────────┴─────────┴────────┘")

def cash():
    while True:
        money_inserted = float(input("\nInsert an amount of money: DH ").strip())
        return money_inserted

def card():
        print("\nInsert your card into the card reader. ")
        print("\n\033[5;30mCommunicating with your bank ...\033[0m")
        print("\nYour card has been approved.") 
        insert_card = True
        print("\nPlease leave the card in the reader and proceed with your purchase(s).")
        return insert_card

def item_choice(menu_selected):
    global item_selected, item_price, item_code    
    while True: 
        number = input("\nEnter the item number of the item you want: ").strip()
        for item in menu_selected:
            if number == str(item['code']):
                item_code = number
                item_selected = item['item']
                item_price = item['price']
                if item['stock'] > 0:
                    break
                else:  
                    print(f"\nSorry, {item['item']} is out of stock.")        ##continue (w/o item)??  
                    break   
        else: 
            print("\nInvalid item number. Please try again.")
        break

# function to update the items stock when one is dispensed
def update_stock(menu_items, item_num):
    # for loop iterates through items in the selected menu 
    for item in menu_items:
        # select the item whose code the user has entered
        if item_num == str(item['code']):
            # deduct the stock for that specific item by 1 
            item['stock'] -= 1           
            # break out of the loop (once selected item stock is deducted)
            break

# function to print item dispensed message and update item stock
def item_dispensed():
    print(f'\nYour {item_selected} has been dispensed.')    
    update_stock(menu_selected, item_code)

def thank_you():
    print("\nThank you for purchasing! Please come again!")

### PROGRAM START!!!

# ask user to input their name
name = input("\nEnter your name: ").strip().title()
# display the title as ASCII Art
print("""
                                
                ┌───────────────────────────────────────────────────────────┐ 
                │  ╦  ╦ ╔═╗ ╔╗╔ ╔╦╗ ╦ ╔╗╔ ╔═╗    ╔╦╗ ╔═╗ ╔═╗ ╦ ╦ ╦ ╔╗╔ ╔═╗  │ 
                │  ╚╗╔╝ ║╣  ║║║  ║║ ║ ║║║ ║ ╦    ║║║ ╠═╣ ║   ╠═╣ ║ ║║║ ║╣   │ 
                │   ╚╝  ╚═╝ ╝╚╝ ═╩╝ ╩ ╝╚╝ ╚═╝    ╩ ╩ ╩ ╩ ╚═╝ ╩ ╩ ╩ ╝╚╝ ╚═╝  │  
                └───────────────────────────────────────────────────────────┘
""")
# greet the user
print(f"Greetings {name}!")
# welcome message
print("WELCOME!")

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

print("\n╔═══════════════════════════════════════╗")
print("║        CHOOSE A PAYMENT METHOD        ║")
print("╠═══════════════════════════════════════╣")
print("║           CASH[1] | CARD[2]           ║")
print("╚═══════════════════════════════════════╝")

while True: 
    payment = input("\nTYPE 1 TO INSERT CASH OR 2 TO USE A CARD: ").strip()    
    if payment == "1":        
        type = "CASH"
        money = cash()
        card_used = False
        break        
    elif payment == "2":         
        type = "CARD"
        card_used = card()
        break    
    else:        
        print("\nInvalid choice. Please enter 1 for cash or 2 for card.")

# print a formatted list of menu types to choose from
print("\n╔══════════════════════════════════════════╗")
print("║          CHOOSE A MENU CATEGORY          ║")
print("╠══════════════════════════════════════════╣")
print("║  SNACKS[1] | BEVERAGES[2] | DESSERTS[3]  ║")
print("╚══════════════════════════════════════════╝")

menu_choice()

