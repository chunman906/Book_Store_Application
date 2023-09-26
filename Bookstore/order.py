from shoppingbasket import *
import json

class Order:
    def __init__(self, items, total_price, user, purchase_date):
        self.items = items
        self.total_price = total_price
        self.user = user
        self.purchase_date = purchase_date

    def display(self):
        print(f'The total price of the bill is £{self.total_price} by the customer <{self.user}>.')
        print(f'It was purchased on {self.purchase_date} for the items: ')
        for item, book_details in self.items.items():
            print(f'Item set - {item}: Book <{book_details["Book"]}>, Quantity:{book_details["Quantity"]}, Price: £{book_details["Price"]} ')

# Help converting the object attribute into dictionary / back to class object
    def to_dict(self):
        return {'items': self.items, 'total_price': self.total_price, 'user': self.user, 'purchase_date': self.purchase_date}

    @classmethod
    def from_dict(cls, data):
        items = ShoppingBasket.from_dict(data['items'])
        return cls(items, data['user'], data['total_price'], data['purchase_date'])
