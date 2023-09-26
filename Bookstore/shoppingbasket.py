from book import *
from bookshelf import *

class ShoppingBasket:
    def __init__(self):
        self.shoppingcart = {}
        self.item_id = 1

# Adding book into the shopping basket
    def add_book(self, book):
        item_basket = {}
        self.shoppingcart[self.item_id] = item_basket
        quantity = int(input('How many quantity you want to buy? \n'))
        item_basket.update({'Book': book.book_name, 'Quantity': quantity, 'Price': book.price*quantity, 'Price_per_item': book.price})
        self.item_id += 1
        print(f'You have added {quantity} quantity of {book.book_name} book for a total of £{book.price*quantity} into the cart. \n')

# Calculate total price
    def total_price(self):
        total_price = 0
        for item, book_details in self.shoppingcart.items():
            total_price += book_details["Price"]
        return total_price

# Display all the items in the shopping basket
    def display(self):
        if self.shoppingcart:
            for item, book_details in self.shoppingcart.items():
                print(f'Item set - {item}: Book <{book_details["Book"]}>, Quantity:{book_details["Quantity"]}, Price: £{book_details["Price"]} ')
        else:
            print('The shopping basket is empty now. ')
        total_price = self.total_price()
        print(f'Total price for the bill is: £{total_price} \n')

# Modify the purchase details of shopping basket
    def modify_cart(self):
        self.display()
        item_choice = int(input('Which item set do you want to modify? Type the item number: \n'))
        item_remove = input('Do you want to remove the book? Type Y / N: \n')
        if item_remove.strip().lower() == 'y':
            print(f'You have successfully removed item set - {item_choice}: Book <{self.shoppingcart[item_choice]["Book"]}.>')
            del self.shoppingcart[item_choice]
        else:
            item_change = input('Do you want to change the quantity of the book? Type Y / N: \n')
            if item_change.strip().lower() == 'y':
                item_quantity = int(input('What is the new quantity ? '))
                self.shoppingcart[item_choice]['Quantity'] = item_quantity
                self.shoppingcart[item_choice]['Price'] = self.shoppingcart[item_choice]['Price_per_item']*item_quantity
                print('You have successfully changed the purchase details.')
            else:
                print("You haven't modify any details. Please try again. ")

# Help converting the object attribute into dictionary / back to class object
    def to_dict(self):
        return self.shoppingcart

    @classmethod
    def from_dict(cls, data):
        basket = cls()
        basket.shoppingcart = data
        return basket
