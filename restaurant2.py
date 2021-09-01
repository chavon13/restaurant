MENU = [["burgers", 10], ["fries", 8], ["onion rings", 8], ["drink", 5]]
print(MENU)

def get_order():
    current_order = []
    while True:
        print("What can I get for you?")
        order = input()
        if order in MENU:
            current_order.append(order)
        else:
            print("We do not have that here.")
        if is_order_complete():
            return current_order

def is_order_complete():
    print("anything else? yes/no")
    choice = input()
    if choice == "no":
        return True
    elif choice == "yes":
        return False
    else:
        print("Please choose from MENU")

print(get_order)
