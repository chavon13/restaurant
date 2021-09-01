class Restaurant:
    def __init__(self, menus = {}, customers = {}, orders = []):
        self.menus = menus
        self.customers = customers
        self.orders = orders
    
    def greeting(self):
        new_cx = {}
        new_cx["name"] = input("Hello there! Can I have your name please?")
        new_cx["number"] = input("May I please have a phone number for your order?")
        self.new_customer(new_cx["name"], new_cx["number"])

    

