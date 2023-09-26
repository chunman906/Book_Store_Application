from book import *
from exception import *
from filemanager import *
import csv
import os

class BookShelf:
    def __init__(self, file):
        self.book_list = []
        self.file = file
        self.book_id = 0
        self.load_book()

# adding the book
    def add_book(self, book):
        self.book_list.append(book)
        self.save_book()


# list all the books
    def list_book(self):
        print(f'Here are the list of the books we have : ')
        self.book_list.sort(key=lambda e_book: e_book.book_id)
        for each_book in self.book_list:
            print(f'BookID: {each_book.book_id} - Book Name <{each_book.book_name}>, genre: {each_book.genre}, author: {each_book.author}, publisher: {each_book.publisher}, price: £{each_book.price} ')

# search for the book
    def find_book(self):
        not_found_book = True
        while not_found_book:
            print(f'How do you want to search the book? \n Option - 1: Author \n Option - 2: ISBN ')
            choice = self.check_int(input('Input option number: '))
            if choice == 1:
                author = input('Type the author name: ').strip().lower()
                author_generator = self.generate_author(author)
                for each_book in author_generator:
                    each_book.display()
                    not_found_book = False
                if not_found_book:
                    print("The name you have entered doesn't match with our system. ")
                    break
            elif choice == 2:
                isbn = input('Type the ISBN: ')
                isbn_generator = self.generate_isbn(isbn)
                for each_book in isbn_generator:
                    each_book.display()
                    not_found_book = False
                if not_found_book:
                    print("The ISBN you have entered doesn't match with our system. ")
                    break
            else:
                print('You have input incorrect option! Try again.')

# show the book information
    def show_book(self):
        self.list_book()
        while True:
            choice = self.check_int(input(f'Which book do you want to read the information? Type the Book ID: \n'))
            if type(choice) == int and choice <= len(self.book_list):
                return self.book_list[choice-1].display()
            else:
                print('You have input a wrong number! Try again. ')

# adding book into sopping basket
    def into_basket(self):
        self.list_book()
        choice = self.check_int(input('Which book do you want to add into the shopping basket? Type the book ID: \n'))
        return self.book_list[choice-1]

# use for validate the integer input
    def check_int(self, input_int):
        try:
            return int(input_int)
        except ValueError as err:
            print(err)

# generator for finding by authors
    def generate_author(self, author):
        for each_book in self.book_list:
            if each_book.author.lower() == author:
                yield each_book

# generator for finding by ISBN
    def generate_isbn(self, isbn):
        for each_book in self.book_list:
            if each_book.isbn == isbn:
                yield each_book

# save book data into csv file
    def save_book(self):
        try:
            if not os.path.exists(self.file):
                raise FileNotFound('The file is not exist!')
            with FileManager(self.file, 'w') as csv_file:
                csv_writer = csv.writer(csv_file)
                for each_book in self.book_list:
                    csv_writer.writerow([each_book.book_name, each_book.author, each_book.isbn, each_book.genre, each_book.publisher, each_book.price])
        except FileNotFound as err:
            print(err)
            logging.error(f'Failed to find {self.file}.')
        else:
            print('Goodbye.The books data has been saved on csv file successfully. ')

# load book data from csv file
    def load_book(self):
        if not os.path.exists(self.file):
            logging.error(f'Failed to open {self.file}.')
            raise FileNotFound('The file is not exist! Make sure the csv file name is correct!')
        with FileManager(self.file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for each_line in csv_reader:
                book_name, author, isbn, genre, publisher, price = each_line
                self.book_id += 1
                self.book_list.append(Book(self.book_id, book_name, author, isbn, genre, publisher, int(price)))

