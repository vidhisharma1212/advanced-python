class Library:
    def __init__(self,listOfBooks):
        self.books= listOfBooks

    def displayAvailableBooks(self):
        print("The books present in this library are: ")
        for book in self.books:
            print("\t *",book)
    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName} . Please keep it neat and handle it properly. Return the book within 30 days.")
            self.books.remove(bookName)
            return True
        elif bookName not in m:
            print("Maybe you have typed with an error... Please recorrect your spelling! ")
        else:
            print("Sorry, the book is currently issued to someone else. Please wait until the borrower returns the book.")
            return False
    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book. Hope you come back !")



class Student:
    def requestBook(self):
        self.book= input("Enter the name of the book you want to borrow: \n")
        return self.book

    def returnBook(self):
        self.book= input("Enter the name of the book you want to return: \n")
        return self.book


if __name__== "__main__":
    m= ["Algorithms", "Math", "Physics", "Physical Education", "How to succeed"]
    centralLibrary= Library(["Algorithms", "Math", "Physics", "Physical Education", "How to succeed"])
    student= Student()
    # centralLibrary.displayAvailableBooks()

    while (True):
        welcomeMsg= '''=====Welcome to Central Library=====
        Press ->
        1. Listing all the books
        2. Request a book
        3. Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        a= int(input("Enter your choice: \n"))
        if a==1:
            centralLibrary.displayAvailableBooks()
        elif a==2:
            centralLibrary.borrowBook(student.requestBook())
        elif a==3:
            centralLibrary.returnBook(student.returnBook())
        elif a==4:
            print("Thanks for choosing us, Have a great day ahead!")
            exit()
        else:
            print("Invalid choice! ")