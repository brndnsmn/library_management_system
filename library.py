class Library:
    def __init__(self, file="books.txt"):
        self.file = open("books.txt", "a+")
        # 'a+' open file for reading and writing (appending at the end of file)
        # the file is created if it does not exist

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)  # seek(0), dosyanın başına giderek okuma işleminin başından itibaren yapılmasını sağlar
        books = self.file.read().splitlines()
        for book in books:
            title, author, year, pages = book.split(',')
            print(f"Title: {title}, Author: {author}, Release Year: {year}, Pages: {pages}")
        print(f"Title: {title}, Author: {author}")

    def add_book(self):
        book_title = input("Enter the name of the book: ")
        book_author = input("Enter the author of the book: ")
        release_year = input("Enter the release year of the book: ")
        book_pages = input("Enter the pages of the book: ")
        line = f"{book_title}, {book_author}, {release_year}, {book_pages}"
        self.file.write(line)
        print(f"Book '{book_title}' by {book_author} added successfully.")

    def remove_book(self):
        book_name = input("Enter the book name that will be deleted: ")
        self.file.seek(0)
        lines = self.file.read().splitlines()
        books_list=[]
        for line in lines:
            books_list.append(line)
        for i, book_info in enumerate(books_list):
            if book_name in book_info:
                del books_list[i]
                break

        self.file.seek(0)
        self.file.truncate()  # Remove contents of the file

        for book_info in books_list:
            self.file.write(book_info + '\n')

        print(f"Book '{book_name}' removed successfully.")


lib = Library()
while True:
    print("*** MENU ***\n 1)List Books\n 2)Add Book\n 3)Remove Book\n ")
    selection = input("Please select a number: ")
    if selection == "1":
        lib.list_books()
    elif selection == "2":
        lib.add_book()
    elif selection == "3":
        lib.remove_book()
    elif selection == "q":
        break
    else:
        print("Invalid selection. Please try again!")








