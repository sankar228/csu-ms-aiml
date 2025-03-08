class ItemToPurchase :
    item_name: str
    item_price: float
    item_quantity: int
    
    def __init__(self, item_name: str, item_price: float, item_quantity: int):
        self.item_name = item_name
        self.item_price= item_price
        self.item_quantity= item_quantity


## Function to print the Total cost        
def print_item_cost(items: list[ItemToPurchase]):
    print()
    print("###########")
    print("TOTAL COST")
    total_cost = 0
    for item in items:
        total_cost += round(float(item.item_quantity * item.item_price), 2)
        print(f"{item.item_name} {item.item_quantity} @ ${pricestr(item.item_price)} = ${pricestr(round(float(item.item_quantity * item.item_price), 2))}")
    
    print(f"Total: ${pricestr(total_cost)}")

def pricestr(v: float) -> str:
    return f"{round(v , 2): .2f}"
                

if __name__ == "__main__":
    items = []
    for i in range(1, 3):
        print(f"Item {i}")
        item_name = input("Enter the item name: ")
        item_price = round(float(input("Enter the item price: $")), 2)
        item_quantity = int(input("Enter the item quantity: "))
        
        items.append(ItemToPurchase(item_name=item_name, item_price=item_price, item_quantity=item_quantity))

    print_item_cost(items=items)        