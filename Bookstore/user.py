from abc import ABC, abstractmethod
from shoppingbasket import *
from order import *
from datetime import datetime
import json


# Abstract Class
class User(ABC):
    def __init__(self):
        self.basket = ShoppingBasket()

    @abstractmethod
    def checkout(self):
        pass


# Implementation Class
class UnregisterUser(User):
    def __init__(self):
        super().__init__()
        self.guest_id = 0

    def checkout(self):
        while True:
            choice = input('Are you confirm to proceed for checkout? Type Y / N: \n')
            if choice.lower() == 'y' or choice.lower() == 'yes':
                basket = self.basket.shoppingcart
                if basket:
                    today = datetime.now().date().strftime('%d-%m-%Y')
                    self.guest_id += 1
                    name = "guest_id_" + str(self.guest_id)
                    total_price = self.basket.total_price()
                    order = Order(basket, total_price, name, today)
                    print('Thanks for your purchase. You have successfully placed the order. \n')
                    order.display()
                    self.basket = ShoppingBasket()
                    break
                else:
                    print('Your basket is empty! Please select item.')
            else:
                print('Type your option again.')
                break


class RegisteredUser(User):
    def __init__(self, firstname, lastname, email_id, password):
        super().__init__()
        self.firstname = firstname
        self.lastname = lastname
        self.__email_id = email_id
        self.__password = password
        self.order_history = []

    @property
    def email_id(self):
        return self.__email_id

    @email_id.setter
    def email_id(self, email_id):
        if '@' in email_id:
            self.__email_id = email_id
        else:
            raise NameIsNotMatch("You have entered incorrect email! Try again. ")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if len(password) >= 8:
            self.__password = password
        else:
            raise PasswordIsNotMatch('Your password should be at least 8 numbers/characters. ')

# To proceed check out for the purchase
    def checkout(self):
        while True:
            choice = input('Are you confirm to proceed for checkout? Type Y / N: \n')
            if choice.lower() == 'y' or choice.lower() == 'yes':
                basket = self.basket.shoppingcart
                if basket:
                    today = datetime.now().date().strftime('%d-%m-%Y')
                    name = self.firstname + " " + self.lastname
                    total_price = self.basket.total_price()
                    order = Order(basket, total_price, name, today)
                    print('Thanks for your purchase. You have successfully placed the order.')
                    self.order_history.append(order)
                    order.display()
                    self.basket = ShoppingBasket()
                    break
                else:
                    print('Your basket is empty! Please select item.')
            else:
                print('Type your option again.')
                break

# View the orders history and sorted by date
    def view_orders_history(self):
        print('Here are the order history records sorted by date: ')
        if self.order_history:
            self.order_history.sort(key=lambda order: order.purchase_date)
            for each_order in self.order_history:
                print("")
                print(f'Purchase Date:{each_order.purchase_date} - Total bill: £{each_order.total_price}')
                for item, book_details in each_order.items.items():
                    print(f'Item set - {item}: Book <{book_details["Book"]}>, Quantity:{book_details["Quantity"]}, Price: £{book_details["Price"]} ')
        else:
            print('The order history is empty now. ')

# View the user's account details
    def view_account_details(self):
        print("")
        print("The user's account details are: ")
        print(f'First name: <{self.firstname}>, Last name: <{self.lastname}>')
        print(f'Email ID: <{self.email_id}>, Password: <{self.password}>')
        history = "Y" if self.order_history else "N"
        print('Order history available: ' + history)

# Modify the user's account details
    def modify_account_details(self):
        choice = input('Do you want to modify the details of first name / last name / email id / password ? \n').strip().lower()
        while True:
            if choice == 'first name' or choice == 'firstname':
                self.firstname = str(input('What is the new first name? \n'))
            elif choice == 'last name' or choice == 'lastname':
                self.lastname = str(input('What is the new last name? \n'))
            elif choice == 'email id' or choice == 'emailid':
                try:
                    self.email_id = str(input('What is the new email ID? \n'))
                except NameIsNotMatch as err:
                    print(err)
                    continue
            elif choice == 'password':
                try:
                    self.password = str(input('What is the new password? \n'))
                except PasswordIsNotMatch as err:
                    print(err)
                    continue
            else:
                print('You have incorrect input! Try again. ')
                break
            print('You have changed the details successfully. \n')
            self.view_account_details()
            break

# Help converting the object attribute into dictionary / back to class object
    def to_dict(self):
        return {
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email_id': self.email_id,
            'password': self.password,
            'order_history': [order.to_dict() for order in self.order_history]
        }

    @classmethod
    def from_dict(cls, json_dict):
        user = cls(json_dict['firstname'], json_dict['lastname'], json_dict['email_id'], json_dict['password'])
        user.order_history = [Order(o['items'], o['total_price'], o['user'], o['purchase_date']) for o in json_dict['order_history']]
        return user

