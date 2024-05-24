from app import books, page_count


USER_CHOICE = '''Enter one of the following

- 'b' to list highest rated books
- 'c' to list cheapest books
- 'n' to display the next available book in the catalogue
- 'p' to display the number of pages
- 'q' to quit

Enter your choice: '''


def print_best_books():
    best_books = sorted(books, key=lambda x: x.rating, reverse=True)[:10]
    for book in best_books:
        print(book)


def print_cheapest_books():
    cheapest_books = sorted(books, key=lambda x: x.price)[:10]
    for book in cheapest_books:
        print(book)


books_generator = (x for x in books)


def print_next_book():
    # available_books = sorted(books, key=lambda x: x.available)
    print(next(books_generator))


def print_page_count():
    print(page_count)


user_choices = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': print_next_book,
    'p': print_page_count
}


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in user_choices:
            user_choices[user_input]()
        user_input = input(USER_CHOICE)


menu()
