def add(cart):
    item = input("Enter product to add: ")
    cart.append(item)
    print(f"'{item}' added to cart.")

def remove(cart):
    item = input("Enter product to remove: ")
    if item in cart:
        cart.remove(item)
        print(f"'{item}' removed from cart")
    else:
        print(f"'{item}' not in cart to remove")

def search(cart):
    item = input("Enter product to search: ")
    if item in cart:
        print(f"Yes, '{item} is in the cart.")
    else:
        print(f"No, '{item} is not in the cart.")

def display(cart):
    print("Cart:",cart)

def count(cart):
    print("Number of products:",len(cart))

cart = []

print("Cart Operations:")
print("1. Add Product")
print("2. Remove Product")
print("3. Search Product")
print("4. Display Cart")
print("5. Count Products")
print("6. Sort the cart (alphabetically)")
print("7. Clear the cart")
print("8. Exit")

while True:
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        add(cart)
    elif choice == 2:
        remove(cart)
    elif choice == 3:
        search(cart)
    elif choice == 4:
        display(cart)
    elif choice == 5:
        count(cart)
    elif choice == 6:
        cart.sort()
        print("Cart is sorted")
    elif choice == 7:
        cart.clear()
        print("Cart is cleared")
    elif choice == 8:
        break
    else:
        print("Invalid choice!\nTry again")