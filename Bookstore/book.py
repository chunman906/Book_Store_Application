class Book:
    def __init__(self, book_id, book_name, author, isbn, genre, publisher, price):
        self.book_id = book_id
        self.book_name = book_name
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.publisher = publisher
        self.price = price

    def display(self):
        print(f'The book <{self.book_name}> is a {self.genre} type of book and written by <{self.author}>.')
        print(f'It has been published by {self.publisher} and the ISBN is {self.isbn}. The price is £{self.price} \n')
