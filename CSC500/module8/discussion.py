class Book:
    def __init__(self, name, author, price, publisher = "SelfWritten"):
        self.publisher = publisher
        self.name = name
        self.author = author
        self.__price = price

    def __call__(self, *args, **kwds):
        print("object call")        
    
    def setprice(self, price):
        self.__price = price
    
    def getprice(self):
        return self.__price

    
if __name__ == "__main__":
   book1 = Book(name="English Book", author="James", price=10)
   book2 = Book(name="Maths Book", author="Toney", price=20)
   
   
   print(f"BookName: {book1.name}, Author: {book1.author}, price: {book1.getprice()}")
   book1.setprice(12)
   print(f"BookName: {book1.name}, Author: {book1.author}, price: {book1.getprice()}")
   
   print(f"BookName: {book2.name}, Author: {book2.author}, price: {book2.getprice()}")

   