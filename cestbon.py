

menu = [["burgers", 10], ["fries", 8], ["onion rings", 8], ["drink", 5]]

print(menu)

class Order:
    def __init__(self, customer = {}, items = [], fulfilled = False):
        self.customer = input("Can I have your name please?")
        self.items = input("What can I get you?")
        self.fulfilled = fulfilled
        wallet = 100
        burgers = 10
        fries = 8
        onion_rings = 8
        drink = 5
        while wallet >= 4:
            if self.items == "burgers":
                burger_total = wallet - burgers
                print(burger_total)
                wallet -= 10
            elif self.items == "fries":
                fries_total = wallet - fries
                print(fries_total)
                wallet -= 8
            elif self.items == "onion_rings":
                onion_rings_total = wallet - onion_rings
                print(onion_rings_total)
                wallet -= 8
            elif self.items ==  "drink":
                drink_total = wallet - drink
                print(drink_total)
                wallet -= 5

            else:
                print("Please enter your order.")

    # def enter_order(self):
    #     return self.items

        



order1 = Order()

    
