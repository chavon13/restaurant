wallet = 100

menu = [["burgers", 10], ["fries", 8], ["onion rings", 8], ["drink", 5]]

print(menu)

class Order:
    def __init__(self, customer = {}, items = [], fulfilled = False):
        self.customer = input("Can I have your name please?")
        self.items = input("What can I get you?")
        self.fulfilled = fulfilled
        if self.items == "burgers":
            print(wallet - 10)
        elif self.items == "fries":
            print(wallet - 8)
        elif self.items == "onion rings":
            print(wallet - 8)
        elif self.items ==  "drink":
            print(wallet - 5)
        else:
            print("Please enter your order.")
    # def enter_order(self):
    #     return self.items

        



order1 = Order()

    
