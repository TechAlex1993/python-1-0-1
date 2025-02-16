# Python classes and objects : Book class

class Book:
    def __init__(self, title, author , price , quantity):
            self.title = title
            self.author = author
            self.price = price
            self.quantity = quantity

    def get_price(self):
        return self.price
    
    def set_price(self, new_price):
         self.price = new_price

    def get_quantity(self):
         return self.quantity
    
    def set_quantity(self, new_quantity):
         self.qunantity = new_quantity
    
    def sell(self, sold_quantity):
         if sold_quantity > self.quantity:
              print("Error: Not enough books in stock.")
         else:
              self.quantity -= sold_quantity
    def restock(self, number_added):
        self.quantity += number_added
        return self.quantity

my_book = Book("The Catcher in the Rye", "J.D. Salinger", 10.99, 5)
print(my_book.get_price())
my_book.set_price(12.99)