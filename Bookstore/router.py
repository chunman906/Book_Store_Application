from bookshelf import *
from usersystem import *
import logging


# Master control panel
class Router:
    def __init__(self):
        self.running = True
        self.bookshelf = BookShelf('books.csv')
        self.user_system = UserSystem('users.JSON')

# Main and beginning menu interface
    def run(self):
        self.logo()
        self.command_view_begin()
        while self.running:
            choice = str(input("Please choose from the <main> menu options. Input the number: \n"))
            if choice == '1':
                self.bookshelf.list_book()
            elif choice == '2':
                self.bookshelf.show_book()
            elif choice == '3':
                register_user = self.user_system.reg_user_login()
                if register_user:
                    self.user_interface(register_user)
            elif choice == '4':
                guest = self.user_system.guest_login()
                if guest:
                    self.guest_interface(guest)
            else:
                print('Bye. See you next time.')
                self.running = False

# menu for customer logged as guest
    def guest_interface(self, user):
        self.guest_logo()
        self.command_view_guest()
        while self.running:
            choice = str(input("Please choose from the <guest> menu options. Input the number: \n"))
            if choice == '1':
                self.bookshelf.find_book()
            elif choice == '2':
                self.bookshelf.list_book()
            elif choice == '3':
                self.bookshelf.show_book()
            elif choice == '4':
                user.basket.add_book(self.bookshelf.into_basket())
            elif choice == '5':
                user.basket.display()
            elif choice == '6':
                user.basket.modify_cart()
            elif choice == '7':
                user.checkout()
            else:
                self.running = False

# menu for customer login as registered user
    def user_interface(self, user):
        self.user_logo(user)
        self.command_view_registered()
        while self.running:
            choice = str(input("Please choose from the <user> menu options. Input the number: \n"))
            if choice == '1':
                self.bookshelf.find_book()
            elif choice == '2':
                self.bookshelf.list_book()
            elif choice == '3':
                self.bookshelf.show_book()
            elif choice == '4':
                user.basket.add_book(self.bookshelf.into_basket())
            elif choice == '5':
                user.basket.display()
            elif choice == '6':
                user.basket.modify_cart()
            elif choice == '7':
                user.checkout()
                self.user_system.save_user()
            elif choice == '8':
                user.view_orders_history()
            elif choice == '9':
                user.view_account_details()
            elif choice == '10':
                user.modify_account_details()
                self.user_system.save_user()
            else:
                self.running = False


    def logo(self):
        print('---------------------------------------------------------------------')
        print(' ')
        print('Welcome to the Book Store application! Lets have a look on our books.')
        print(' ')
        print('---------------------------------------------------------------------')

    def command_view_begin(self):
        print('1. View the list of our book.')
        print('2. View the individual book basic details')
        print('3. Log in / Register account')
        print('4. Continue as guest')
        print('<Press any other key to exit the application.> ')
        print('<System message>: You will need to log in as user / guest to explore more option. \n')

    def command_view_guest(self):
        print('1. Search for the book by author or ISBN.')
        print('2. View the list of our book.')
        print('3. View the individual book basic details')
        print('4. Add book to shopping basket.')
        print('5. View the shopping basket.')
        print('6. Modify the shopping basket.')
        print('7. Proceed to checkout and make payment.')
        print('<Press any other key to exit the application.> ')

    def guest_logo(self):
        print('---------------------------------------------------------------------')
        print(' ')
        print('Welcome to logged as guest to shopping in our store.')
        print(' ')
        print('---------------------------------------------------------------------')

    def user_logo(self, user):
        print('---------------------------------------------------------------------')
        print(' ')
        print(f'Welcome back, {user.firstname} {user.lastname}! Enjoy shopping in our store.')
        print(' ')
        print('---------------------------------------------------------------------')

    def command_view_registered(self):
        print('1. Search for the book by author or ISBN.')
        print('2. View the list of our book.')
        print('3. View the individual book basic details')
        print('4. Add book to shopping basket.')
        print('5. View the shopping basket.')
        print('6. Modify the shopping basket.')
        print('7. Proceed to checkout and make payment.')
        print('8. Access the order history')
        print('9. View the user account details')
        print('10. Modify the user account details')
        print('<Press any other key to exit the application.> ')



