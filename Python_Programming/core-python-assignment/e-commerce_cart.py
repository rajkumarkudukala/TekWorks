def total(items):
    sum = 0
    if(len(items) == 0):
        print("Empty Cart!")
    elif len(items) > 5:
        for i in items:
            sum+=items[i]
        sum-=sum*10/100
    else:
        for i in items:
            sum+=items[i]
    return sum

items = {}
num_entries = int(input("Enter the number of items in the cart: "))

for _ in range(num_entries):
    key = input("Enter the item name: ")
    value = int(input("Enter the price: "))
    items[key] = value

print("Total Price:",total(items))