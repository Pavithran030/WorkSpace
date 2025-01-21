# Initialize an empty dictionary to represent the bookstore inventory
inventory = {}

while True:
    print("\n1. Add new book")
    print("2. Update book quantity")
    print("3. Display inventory\n4. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        title = input("\nEnter the title of the book: ")
        quantity = int(input("Enter the quantity of the book: "))
        if title in inventory:
            inventory[title] += quantity
        else:
            inventory[title] = quantity

    elif choice == 2:
        title = input("\nEnter the title of the book to update: ")
        if title in inventory:
            quantity = int(input("Enter the new quantity: "))
            inventory[title] = quantity
        else:
            print("Book not found in inventory.")

    elif choice == 3:
        print("\nCurrent Inventory:")
        for title, quantity in inventory.items():
            print(f"Title: {title}, Quantity: {quantity}")

    elif choice == 4:
        print("\nExiting the program.")
        break

    else:
        print("\nInvalid choice. Please enter a number between 1 and 4.")
