def main():
    print("Food Bill details")
    foodprice = round(float(input("Please enter the food price: ")), 2)
    
    if (foodprice == None or foodprice <= 0):
        print("Invalid food price")
        exit(1)
    
    tip_amount =  round(foodprice * (18/100), 2)
    sales_tax = round(foodprice * (7/100), 2)
    
    total_price = round(foodprice + tip_amount + sales_tax, 2)
    
    print(f"Food price: ${foodprice}")
    print(f"Tip: ${tip_amount}")
    print(f"Sales Tax: ${sales_tax}")
    print(f"Total price: ${total_price}")
    

if __name__ == '__main__':
    main()