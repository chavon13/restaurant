wallet = 100

menu = [["burgers", 10], ["fries", 8], ["onion rings", 8], ["drink", 5]]

print(menu)

class Order:
    def __init__(self, items = [], customer = {}, fulfilled = False):
        self.items = input("What can I get you?")
        self.customer = input("Can I have your name please?")
        self.fulfilled = fulfilled
    def enter_order(self):
        return self.items


order1 = Order()
order1.enter_order
    
