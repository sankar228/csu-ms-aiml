
class ItemToPurchase:
    def __init__(self, item_name= None, item_disc= None, price= None, quantity= None):
        self.item_name = item_name
        self.ite_disc = item_disc
        self.price = price
        self.quantity = quantity
    
    
    
class ShoppingCart:
    
    def __init__(self, customer_name= None, current_date= "January 1, 2020", cart_items= []):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items
        
    
    def add_item(self, item: ItemToPurchase):
        self.cart_items.append(item)
        print(f"item: {item.item_name} added to the cart")
    
    def remove_item(self, item_name):
        for item in self.cart_items:
            if (item.item_name == item_name):
                self.cart_items.remove(item)
                print(f"item: {item_name} removed from the cart")
                return
        print(f"Item: {item_name} not found in cart. Nothing removed.")
    
    def modify_item(self, updated_item: ItemToPurchase):
        for item in self.cart_items:
            if (item.item_name == updated_item.item_name):
                # Update the item details
                if(updated_item.ite_disc != None):
                    item.ite_disc = updated_item.ite_disc
                elif (updated_item.price != None):
                    item.price = updated_item.price
                elif (updated_item.quantity != None):
                    item.quantity = updated_item.quantity
                else:
                    print(f"No updates available for the item: {updated_item.item_name}")  
                      
                print(f"item: {updated_item.item_name} modified")
                return
            
        print(f"Item:{updated_item.item_name} not found in cart. Nothing modified.")
    
    def get_num_items_in_cart(self) -> int:
        return len(self.cart_items)
    
    def get_cost_of_cart(self) -> float:
        if (self.get_num_items_in_cart() == 0):
            print("SHOPPING CART IS EMPTY")
        else:
            total_price = 0
            for item in self.cart_items:
                total_price += (item.quantity * item.price)
            
            return total_price
    
    def print_total(self):
        print("OUTPUT SHOPPING CART")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {len(self.cart_items)}")
        
        total_price = 0
        for item in self.cart_items:
            total_price += (item.quantity * item.price)
            print(f"{item.item_name} {item.quantity} @ {item.price} = ${item.quantity * item.price}")
        
        print(f"Total: ${total_price}")
    
    def print_descriptions(self):
        print("OUTPUT ITEMS' DESCRIPTIONS")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            total_price += (item.quantity * item.price)
            print(f"{item.item_name}: {item.disc}")

### Main Execution starts here
def menu_items():
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item description, price, and/or quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    
def print_menu():
    menu_items()
    
    customer_name = input("Customer Name: ").strip()
    cart = ShoppingCart(customer_name=customer_name)
    while True:
        menu_option = input("Choose an option:").strip()
        if(menu_option == "q"):
            exit(1)
        elif(menu_option == "a"):
            item_name = input("Enter item name: ").strip()
            item_desc = input("Enter item description: ").strip() or None
            price = input("item price: ").strip()
            price = round(float(price), 2) if price else None
            
            quantity= input("quantity: ").strip()
            quantity = int(quantity) if quantity else None
            
            item = ItemToPurchase(item_name=item_name,item_disc=item_desc, price=price, quantity=quantity)
            cart.add_item(item)
            
        elif(menu_option == "r"):
            item_name = input("Enter item name to remove: ").strip()
            cart.remove_item(item_name)
        elif(menu_option == "c"):
            item_name = input("Enter item name to modify: ").strip()
            item_desc = input("Enter item description: ").strip() or None
            
            price = input("item price: ").strip()
            price = round(float(price), 2) if price else None
            
            quantity= input("quantity: ").strip()
            quantity = int(quantity) if quantity else None
            
            updated_item = ItemToPurchase(item_name=item_name, item_disc=item_desc, price=price, quantity=quantity)
            cart.modify_item(updated_item)
        elif(menu_option == "i"):
            cart.print_descriptions
        elif(menu_option == "o"):
            cart.print_total()
        else:
            print("plase enter valid choice:")
            menu_items()
        
    

if __name__ == "__main__":
    print_menu()