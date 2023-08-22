import math

def main():
    library = {}
    collections = {}
    while True:
        print_menu()
        option = input('\nChoose a menu option: ')
        if option == '1':
            add_books(library)
        elif option == '2':
            print_books(library)
        elif option == '3':
            create_collections(collections, library)
        elif option == '4':
            sort_collections(collections, library)
        elif option == '5':
            delete_collection(collections)
        elif option == '6':
            print("End", end='')
            break
        else:
            print('\nInvalid entry\n')


def print_menu():
    print("\n*******************Main Menu*******************")
    print("1. Add books to the library")
    print("2. Print available books in the library")
    print("3. Create book collections")
    print("4. Sort books in the collections")
    print("5. Delete a collection")
    print("6. Quit")
    print("***********************************************")

def check_isbn(isbn, library):
    if not isbn.isdigit() or len(isbn) != 10:
        return False
    elif isbn in [book["ISBN"] for book in library.values()]:
        return False
    else:
        return True

# Option 1
def add_books(library):
    number_of_books = int(input("How many books would you like to enter: "))
    print()
    
    for n in range(number_of_books):
        while True:
            user_book_title = input(f"Enter book {n+1}: ").split()
            user_ISBN = user_book_title[-1]
            title = " ".join(user_book_title[:-1])
        
            if check_isbn(user_ISBN, library):
                if user_ISBN in library:
                    print("Invalid entry") 
                else:
                    library[user_ISBN] = {
                        "Title": title,
                        "ISBN": user_ISBN
                    }
                break
            else:
                print("Invalid entry")
                continue

# Option 2
def print_books(library):
    print("\nBooks available in the library:")
    for book in library.values():
        print(f"{book['Title']:<20} {book['ISBN']:<20}")

# Option 3
def create_collections(collections, library):
    number_of_collections = int(input("What is the size of the collection? "))
    total_books = len(library)

    for i in range(number_of_collections):
        collection_name = f"Collection {i + 1}"
        print(f"\nEnter the book ISBNs for {collection_name}:")
        books_in_collection = []
        books_entered = 0

        while books_entered < number_of_collections and books_entered < total_books:
            isbn_input = input().strip()

            if isbn_input not in library:
                print(f"Invalid entry")
            else:
                books_in_collection.append(library[isbn_input])
                books_entered += 1

        if len(books_in_collection) == 0:
            print(f"Invalid entry")
            break

        collections[collection_name] = books_in_collection
        total_books -= books_entered
        
    print("\nCurrent book collections:")
    for collection_name, books in collections.items():
        print(f"{collection_name}:")
        for book in books:
            print(f"{book['Title']:<20} {book['ISBN']:<20}")
                    
# Option 4
def sort_collections(collections, library):
    sort_order = input("Sort books in ascending or descending order of ISBN: ")
    for collection_name, books in collections.items():
        sorted_books = sorted(books, key=lambda x: x["ISBN"], reverse=(sort_order == 'descending'))
        collections[collection_name] = sorted_books

    print("\nCurrent book collections:")
    for collection_name, books in collections.items():
        print(f"{collection_name}:")
        for book in books:
            print(f"{book['Title']:<20} {book['ISBN']:<20}") 

# Option 5
def delete_collection(collections):
    collection_to_delete = input("Which collection would you like to delete? ")
    collection_name = f"Collection {collection_to_delete}"
    if collection_name in collections:
        del collections[collection_name]
    else:
        print(f"Invalid entry")

    print("\nCurrent book collections:")
    for collection_name, books in collections.items():
        print(f"{collection_name}:")
        for book in books:
            print(f"{book['Title']:<20} {book['ISBN']:<20}")

main()
