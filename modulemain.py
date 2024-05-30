#Building a Modular Online Bookstore System
#Task 1:Designing the Book Module

#Book class with initiated values
class Book:
    def __init__(self, bookID, title, author, amount):
        self.bookID = bookID
        self.title = title
        self.author = author
        self.amount = amount
    
    def get_bookID(self):
        return self.bookID
    
    def get_title(self):
        return self.title

    def get_author(self):
        return self.author
    
    def get_amount(self):
        return self.amount

    def set_bookID(self, bookID):
        self.bookID = bookID
    
    def set_title(self, new_title):
        self.title = new_title

    def set_author(self, new_author):
        self.author = new_author

    def set_amount(self, new_amount):
        self.amount = new_amount

    #Function used to add books to the list, in dictionary style
    def add_books(books):
        bookID = int(input("Enter 3 digit book ID: "))
        if bookID not in books:
            bookID = input("Enter 3 digit ID of book: ")
            title = input("Enter title of book: ")
            author = input("Enter author of book: ")
            amount = int(input("Enter amount of this book being added to stock: "))
            books[bookID] = Book(bookID, title, author, amount)
            print(f"For ID {books[bookID].get_bookID()}, title: {books[bookID].get_title()} author: {books[bookID].get_author()} amount: {books[bookID].get_amount()} to book inventory. ")
            #print(f"For book ID {books[bookID]}: we have ")
        else:
            print(f"{bookID} is in the database.")

    #Function used to update the title, author, and amount of books in the books list
    def update_books(books):
        bookID = input("Enter book ID: ")
        if bookID in books:
            updateitem = input("Enter a to update book title, b to update book author, or c to update book amounts.")
            if updateitem is "a":
                new_title = input("Enter updated title: ")
                Book.set_title = new_title
                print(f"Updated book title is {books[bookID].get_title()}")
            if updateitem is "b":
                new_author = input("Enter updated author name: ")
                Book.set_author = new_author
                print(f"Updated book title is {books[bookID].get_author()}")
            if updateitem is "c":
                new_amount = input("Enter updated amount of books: ")
                Book.set_amount = new_amount
                print(f"Updated book title is {books[bookID].get_amount()}")
            print(f"{updateitem} entered is not valid.") 
        else:
            print(f"{bookID} entered is not found in books.")   

#Main program used to run the bookstore options
def main():
    books = {}
    while True:
        print("Welcome to the bookstore!")
        print("Choices are 1 for adding books, 2 for updating books")
        print("3 for purchasing book, and 4 to exit program. ")
        choice = int(input("Enter numbers 1, 2, 3 or 4 for action needed: "))
        try:
            if choice == 1:
                Book.add_books(books)
            if choice == 2:
                Book.update_books(books)
            if choice == 3:
                exit()
        except ValueError as e:
            print("Choice {choice} entered is not valid.")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()


