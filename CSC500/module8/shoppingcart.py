
## Cart Item object
class ItemToPurchase :
    item_name: str
    item_desc: str
    item_price: float
    item_quantity: int
    
    def __init__(self, item_name= None, item_desc=None, item_price= 0, item_quantity= 0):
        self.item_name = item_name
        self.item_desc = item_desc
        self.item_price= item_price
        self.item_quantity= item_quantity


    ## Function to print the Total cost        
    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${pricestr(self.item_price)} = ${pricestr(round(float(self.item_quantity * self.item_price), 2))}")
    

    
## Shopping Cart object, contains utility functions to dd, remove, modify and print the Cart items 
class ShoppingCart:
    
    def __init__(self, customer_name= None, current_date= "January 1, 2020", cart_items= []):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items
        
    # Add item to the cart
    def add_item(self, item: ItemToPurchase):
        self.cart_items.append(item)
        print(f"item: {item.item_name} added to the cart")
    
    # Remove item from the Cart
    def remove_item(self, item_name: str):
        for item in self.cart_items:
            if (item.item_name == item_name):
                
                ## Logic to ask the user to input how many quantity of the item to remove from the cart
                ## if the input quantity is more than available in the cart, it will remove the item but no error
                remove_quantity = int(input(f"Cart item {item.item_name} has {item.item_quantity} quantity, How many you want to remove: "))
                if(not validate_item_data(item_quantity=remove_quantity)):
                    return
                if(remove_quantity < item.item_quantity):
                    item.item_quantity = item.item_quantity - remove_quantity
                    self.modify_item(item)
                    return
                if(remove_quantity >= item.item_quantity):
                    self.cart_items.remove(item)
                    print(f"item: {item_name} removed from the cart\n\n")
                    return
                
        print(f"Item: {item_name} not found in cart. Nothing removed.\n\n")
    
    # Modify the existing item from the Cart
    def modify_item(self, updated_item: ItemToPurchase):
        for item in self.cart_items:
            if (item.item_name == updated_item.item_name):
                is_updated = False
                # Update the item details
                if(updated_item.item_desc != None):
                    item.item_desc = updated_item.item_desc
                    is_updated = True
                if (updated_item.item_price != None):
                    item.item_price = updated_item.item_price
                    is_updated= True
                if (updated_item.item_quantity != None):
                    item.item_quantity = updated_item.item_quantity
                    is_updated = True
                
                if(not is_updated):
                    print(f"No updates available for the item: {updated_item.item_name}\n\n")  
                      
                print(f"item: {updated_item.item_name} modified\n\n")
                return
            
        print(f"Item:{updated_item.item_name} not found in cart. Nothing modified.\n\n")
    
    # Get total number of items from the Cart
    def get_num_items_in_cart(self) -> int:
        return len(self.cart_items)
    
    # Total cost of the itesm in the Cart
    def get_cost_of_cart(self) -> float:
        if (self.get_num_items_in_cart() == 0):
            print("SHOPPING CART IS EMPTY")
            return 0
        else:
            total_price = 0
            for item in self.cart_items:
                total_price += (item.item_quantity * item.item_price)
            
            return round(total_price, 2)
        
    # Search for item in the cargt
    def is_item_exist(self, itemname) -> bool:
        for item in self.cart_items:
            if (item.item_name == itemname):
                return True
        return False
   
    # Show the Cart item details
    def print_total(self):
        print("OUTPUT SHOPPING CART")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {len(self.cart_items)}")
        
        for item in self.cart_items:
            print(f"{item.item_name} {item.item_quantity} @ ${round(item.item_price, 2): .2f} = ${round(item.item_quantity * item.item_price, 2): .2f}")
        
        print(f"Total: ${self.get_cost_of_cart(): .2f}\n\n")
    
    # Show the Cart item and its description
    def print_descriptions(self):
        print("OUTPUT ITEMS' DESCRIPTIONS")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        if (self.get_num_items_in_cart() == 0):
            print("SHOPPING CART IS EMPTY")
            return
        
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_desc}")

        print("\n\n")

### Main Execution starts here

# Format output float values
def pricestr(self, v: float) -> str:
    return f"{round(v , 2): .2f}"
    
# validate input values
def validate_item_data(item_price= None, item_quantity= None) -> bool:
    is_valid_date = True
    if (item_price != None and item_price < 0):
        print(f"please enter valid price")
        is_valid_date = False
    if (item_quantity != None and item_quantity <= 0):
        print(f"please enter valid quantity")
        is_valid_date = False
    
    return is_valid_date
        

# Print Menu
def menu_items():
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item description, price, and/or quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    print("*****************************\n\n")

# Print the Menu and promt user to input the operation to perform, like add, remove, modify, print the Cart details
# optionally we can input 'q' to quit the execution    
def print_menu():

    customer_name = input("Enter customer's name: ").strip()
    current_date = input("Enter today's date (eg: February 1, 2020): ").strip()
    cart = ShoppingCart(customer_name=customer_name, current_date=current_date)
    while True:
        print("\n")
        menu_items()
        menu_option = input("Choose an option from Menu: ").strip()
        if(menu_option == "q"):
            exit(1)
        elif(menu_option == "a"):
            print("ADD ITEM TO CART")
            item_name = input("Enter item name: ").strip()
            
            # item name is mandatory field in the cart
            if(item_name == None or item_name == ""):
                print("Item name can not be null")
                continue
            
            # Check if the item already exist in the cart
            if(cart.is_item_exist(itemname=item_name)):
                item_quantity = int(input(f"Item {item_name} already exist in the cart, please enter the extra quantity required: "))
                # validate the price and quantity values
                if(not validate_item_data(item_price=item_price, item_quantity= item_quantity)):
                    continue
                item.item_quantity += item_quantity
                
            else:
                item_desc = input("Enter item description: ").strip() or None
                
                item_price = input("Enter the item price: $").strip()
                item_price = round(float(item_price), 2) if item_price else None
                
                item_quantity= input("Enter the item quantity: ").strip()
                item_quantity = int(item_quantity)
            
                # validate the price and quantity values
                if(not validate_item_data(item_price=item_price, item_quantity= item_quantity)):
                    continue
                
                item = ItemToPurchase(item_name=item_name, item_desc=item_desc, item_price=item_price, item_quantity=item_quantity)
                cart.add_item(item)
            
        elif(menu_option == "r"):
            print("REMOVE ITEM FROM CART")
            if (cart.get_num_items_in_cart() == 0):
                print("SHOPPING CART IS EMPTY")
                continue
            
            item_name = input("Enter item name to remove: ").strip()
            cart.remove_item(item_name)
        elif(menu_option == "c"):
            print("CHANGE ITEM QUANTITY")
            if (cart.get_num_items_in_cart() == 0):
                print("SHOPPING CART IS EMPTY")
                continue
            
            item_name = input("Enter the item name: ").strip()
            
            if(cart.is_item_exist(itemname=item_name)):
                item_quantity= input("Enter the new quantity: ").strip()
                item_quantity = int(item_quantity) if item_quantity else None
                
                updated_item = ItemToPurchase(item_name=item_name, item_quantity=item_quantity)
                cart.modify_item(updated_item)
            else:
                print(f"item: {item_name} not found in cart. Nothing modified.")
        elif(menu_option == "i"):
            cart.print_descriptions()
        elif(menu_option == "o"):
            cart.print_total()
        else:
            print("plase enter valid choice:")
        
    

## Main Function call
if __name__ == "__main__":
    print_menu()