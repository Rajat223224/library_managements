# Define library dictionary
library = {}

# Define function to display menu
def display_menu():
    print('Options:')
    print('1. Add book')
    print('2. Remove book')
    print('3. Search for book')
    print('4. Quit')

# Define function to add a book
def add_book():
    title = input('Enter book title: ')
    author = input('Enter author name: ')
    library[title] = author
    print(f'Added {title} by {author} to the library.')

# Define function to remove a book
def remove_book():
    title = input('Enter book title: ')
    if title in library:
        del library[title]
        print(f'Removed {title} from the library.')
    else:
        print(f'Sorry, {title} is not in the library.')

# Define function to search for a book
def search_book():
    title = input('Enter book title: ')
    if title in library:
        print(f'{title} by {library[title]}')
    else:
        print(f'Sorry, {title} is not in the library.')

# Main loop
while True:
    display_menu()
    choice = input('Enter choice (1-4): ')
    if choice == '1':
        add_book()
    elif choice == '2':
        remove_book()
    elif choice == '3':
        search_book()
    elif choice == '4':
        break
    else:
        print('Invalid choice. Please try again.')
