from collections import defaultdict
class Ammajaan:
    store_name = 'Ammajaan Apple Care'
    MD = 'Mr.X'
    address = 'Goa,High Court Road'
    cno = 7539625841
    stock = {
        "iphone13": 25,
        "iphone13pro": 20,
        "iphone13promax": 15,
        "iphone14": 25,
        "iphone14pro": 20,
        "iphone14promax": 15,
        "iphone15": 25,
        "iphone15pro": 20,
        "iphone15promax": 15,
    }
    price = {
        "iphone13": 60000,
        "iphone13pro": 70000,
        "iphone13promax": 90000,
        "iphone14": 70000,
        "iphone14pro": 80000,
        "iphone14promax": 100000,
        "iphone15": 80000,
        "iphone15pro": 100000,
        "iphone15promax": 130000,
    }

    def __init__(self, name, pno, email, add):
        self.name = name
        self.pno = pno
        self.email = email
        self.add = add
        self.cart = defaultdict(int)

    def add_item(self, item, count=1):
        if item in self.stock:
            if self.stock[item] >= count:
                self.cart[item] += count
                Ammajaan.stock[item] -= count
            else:
                print("We dont have the no of units")
                print(f"The available units are {self.stock[item]}")
        else:
            print("Sorry sir/Ma'am we don't sell that product")

    def remove_item(self, item, count=1):
        if item in self.cart:
            if self.cart[item] >= count:
                self.cart[item] -= count
                Ammajaan.stock[item] += count
                if self.cart[item] == 0:
                    self.cart.pop(item)
            else:
                print(f"your cart contains only {self.cart[item]} {item}")
        else:
            print('Item not found in cart')


c1 = Ammajaan('allen', 7894561235, 'allen@gmail.com', 'BBSR')
c1.add_item('iphone13', 5)
c1.add_item('iphone15', 2)