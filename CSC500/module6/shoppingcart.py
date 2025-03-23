
## Cart Item object
class ItemToPurchase:
    def __init__(self, item_name= None, item_disc= None, price= None, quantity= None):
        self.item_name = item_name
        self.ite_disc = item_disc
        self.price = price
        self.quantity = quantity
    
    
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
    def remove_item(self, item_name):
        for item in self.cart_items:
            if (item.item_name == item_name):
                
                ## Logic to ask the user to input how many quantity of the item to remove from the cart
                ## if the input quantity is more than available in the cart, it will remove the item but no error
                remove_quantity = int(input(f"Cart item {item.item_name} has {item.quantity} quantity, How many you want to remove: "))
                if(not validate_item_date(quantity=remove_quantity)):
                    return
                if(remove_quantity < item.quantity):
                    item.quantity = item.quantity - remove_quantity
                    self.modify_item(item)
                    return
                if(remove_quantity >= item.quantity):
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
                if(updated_item.ite_disc != None):
                    item.ite_disc = updated_item.ite_disc
                    is_updated = True
                if (updated_item.price != None):
                    item.price = updated_item.price
                    is_updated= True
                if (updated_item.quantity != None):
                    item.quantity = updated_item.quantity
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
        else:
            total_price = 0
            for item in self.cart_items:
                total_price += (item.quantity * item.price)
            
            return total_price
        
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
        
        total_price = 0
        for item in self.cart_items:
            total_price += (item.quantity * item.price)
            print(f"{item.item_name} {item.quantity} @ ${round(item.price, 2): .2f} = ${round(item.quantity * item.price, 2): .2f}")
        
        print(f"Total: ${round(total_price, 2): .2f}\n\n")
    
    # Show the Cart item and its description
    def print_descriptions(self):
        print("OUTPUT ITEMS' DESCRIPTIONS")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.ite_disc}")

        print("\n\n")

### Main Execution starts here

# validate input values
def validate_item_date(price= None, quantity= None) -> bool:
    is_valid_date = True
    if (price != None and price < 0):
        print(f"please enter valid price")
        is_valid_date = False
    if (quantity != None and quantity <= 0):
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

    customer_name = input("Please enter your Name: ").strip()
    cart = ShoppingCart(customer_name=customer_name)
    while True:
        print("\n")
        menu_items()
        menu_option = input("Choose an option from Menu: ").strip()
        if(menu_option == "q"):
            exit(1)
        elif(menu_option == "a"):
            item_name = input("Enter item name: ").strip()
            
            # item name is mandatory field in the cart
            if(item_name == None or item_name == ""):
                print("Item name can not be null")
                continue
            
            # Check if the item already exist in the cart
            if(cart.is_item_exist(itemname=item_name)):
                quantity = int(input(f"Item {item_name} already exist in the cart, please enter the extra quantity required: "))
                # validate the price and quantity values
                if(not validate_item_date(price=price, quantity= quantity)):
                    continue
                item.quantity += quantity
                
            else:
                item_desc = input("Enter item description: ").strip() or None
                
                price = input("item price: $").strip()
                price = round(float(price), 2) if price else None
                
                quantity= input("quantity: ").strip()
                quantity = int(quantity)
            
                # validate the price and quantity values
                if(not validate_item_date(price=price, quantity= quantity)):
                    continue
                
                item = ItemToPurchase(item_name=item_name,item_disc=item_desc, price=price, quantity=quantity)
                cart.add_item(item)
            
        elif(menu_option == "r"):
            item_name = input("Enter item name to remove: ").strip()
            cart.remove_item(item_name)
        elif(menu_option == "c"):
            item_name = input("Enter item name to modify: ").strip()
            
            if(cart.is_item_exist(itemname=item_name)):
                item_desc = input("Enter item description: ").strip() or None
                
                price = input("item price: ").strip()
                price = round(float(price), 2) if price else None
                
                quantity= input("quantity: ").strip()
                quantity = int(quantity) if quantity else None
                
                updated_item = ItemToPurchase(item_name=item_name, item_disc=item_desc, price=price, quantity=quantity)
                cart.modify_item(updated_item)
            else:
                print(f"item: {item_name} not found in the shopping cart")
        elif(menu_option == "i"):
            cart.print_descriptions()
        elif(menu_option == "o"):
            cart.print_total()
        else:
            print("plase enter valid choice:")
        
    

## Main Function call
if __name__ == "__main__":
    print_menu()