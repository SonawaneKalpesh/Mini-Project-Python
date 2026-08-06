inventory = {}
while True:
    print("Welcome Inventory Program")
    print("")
    print("1. Add Product")
    print("2. Update Product")
    print("3. Search Product")
    print("4. Delete Product")
    print("5. View Inventory")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        product_name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        inventory[product_name] = {'quantity': quantity, 'price': price}
        print(f"{product_name} added to inventory.")

    elif choice == '2':
        product_name = input("Enter product name to update: ")
        if product_name in inventory:
            quantity = int(input("Enter new quantity: "))
            price = float(input("Enter new price: "))
            inventory[product_name] = {'quantity': quantity, 'price': price}
            print(f"{product_name} updated in inventory.")
        else:
            print(f"{product_name} not found in inventory.")

    elif choice == '3':
        product_name = input("Enter product name to search: ")
        if product_name in inventory:
            print(f"{product_name}: Quantity: {inventory[product_name]['quantity']}, Price: {inventory[product_name]['price']}")
        else:
            print(f"{product_name} not found in inventory.")

    elif choice == '4':
        product_name = input("Enter product name to delete: ")
        if product_name in inventory:
            del inventory[product_name]
            print(f"{product_name} deleted from inventory.")
        else:
            print(f"{product_name} not found in inventory.")

    elif choice == '5':
        if inventory:
            print("Inventory:")
            for product_name, details in inventory.items():
                print(f"{product_name}: Quantity: {details['quantity']}, Price: {details['price']}")
        else:
            print("Inventory is empty.")

    elif choice == '6':
        print("Exiting Inventory Program. Thank you!")
        break
    else:
        
        print("Invalid choice. Please enter a number between 1 and 6.")