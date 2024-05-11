#initialize empty list[], set(), and dictionary{}
books_list = []
authors_set = set()
books_dict = {}

# add book and its author
books_list.append("Python Programming")
authors_set.add("John Smith")
books_dict["Python Programming"] = "John Smith"

books_list.append("Data Structure And Alogrithm")
authors_set.add("John Doe")
books_dict["Data Structre And Alogrithm"] = "John Deo"

books_list.append("Machine Learnig Basic")
authors_set.add("Alice Johnson")
books_dict["Machine learning basic"] = "Alice Johnson"

books_list.append("History Of Bhutan")
authors_set.add("Jigme Namgyel")
books_dict["History Of Bhutan"] = "Jigme Namgyel"

#User input to search book
search_title = input("Hello la! Enter the tile of the book you wanted:").capitalize
if search_title in books_list:
    print(f"Book has been founded! Author is {books_dict[search_title]}")

else:
    print("Sorry la! book not found")

# to display all books
print("List of books available are:")
for book in books_list:
    print(book)

# to remove book
remove_tilte= input("Enter the name of book you wanted to remove:").capitalize
if remove_tilte in books_list:
    remove_author = books_dict[remove_tilte]
    books_list.remove(remove_tilte)
    authors_set.remove(remove_author)
    del books_dict[remove_tilte]
    print("Book removed successfully!")
    print('books available', books_list)

else:
    print("Book not founed")



