### Utility App | VENDING MACHINE

# import the time module (to access the time.sleep function)
import time

# function to use the time.sleep function
def pause():
    # 1-second pause
    time.sleep(1)

# function to print a styled box asking for user's preffered payment method
def payment_method():
    print("""\n\t╔═══════════════════════════════════════╗
\t║        CHOOSE A PAYMENT METHOD        ║
\t╠═══════════════════════════════════════╣
\t║           CASH[1] | CARD[2]           ║
\t╚═══════════════════════════════════════╝\033[0m""")
    pause()

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

payment_method()

# while loop to ensure valid payment method is entered
while True: 
    # ask user if they want to use cash or card
    payment = input("\nCASH OR CARD?: ").strip()   
    # if user inputs 1, payment method is cash 
    if payment == "1":  
        # set variable card_used to False
        card_used = False  
        # while loop to ensure valid amount is inserted
        while True:
            # ask user to insert money (strip removes extra spaces)
            money_inserted = input("\nInsert an amount of money: DH ").strip()
            # tests this block of code
            try:
                # money inserted is converted to float and set to money variable
                money = float(money_inserted)
                # if money is more than 0
                if money > 0:
                    # call the pause() function
                    pause()
                    # set cash equal to money 
                    cash = money
                    # print the balance to be ued for purchase(s)
                    print(f"\nBalance = DH {money:.2f}")
                    # call the pause() function
                    pause()
                    # break out of while loop
                    break
                # if money inserted is less than or equal to 0
                else:
                    # print enter amount more than 0
                    print("\nPlease enter an amount greater than 0.")
            # handles error in inserting money
            except ValueError:
                # print enter a valid amount of money
                print("\nInvalid input. Please enter a valid amount.")    
        # break out of outer while loop
        break  
    # if user inputs 2, payment method is card
    elif payment == "2":         
        # set cash to 0
        cash = 0
        # these statements are used to make the program seem more realistic
        print("\nInsert your card into the card reader. ")
        pause()
        print("\n\033[5;30mCommunicating with your bank ...\033[0m")
        pause()
        print("\nYour card has been approved.") 
        # set card_used to True
        card_used = True
        pause()
        # more realistic (even though there is no physical card)
        print("\nPlease leave the card in the reader and proceed with your purchase(s).")
        pause()
        # break out of outer while loop
        break  
    # runs when invalid payment method is entered  
    else:        
        print("\nInvalid choice. Please enter 1 for cash or 2 for card.")     

# print a formatted list of menu types to choose from
print("\n╔══════════════════════════════════════════╗")
print("║          CHOOSE A MENU CATEGORY          ║")
print("╠══════════════════════════════════════════╣")
print("║  SNACKS[1] | BEVERAGES[2] | DESSERTS[3]  ║")
print("╚══════════════════════════════════════════╝")

menu_choice()